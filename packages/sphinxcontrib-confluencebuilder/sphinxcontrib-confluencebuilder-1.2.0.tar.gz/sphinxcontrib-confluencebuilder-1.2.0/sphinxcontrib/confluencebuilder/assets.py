# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2018-2019 by the contributors (see AUTHORS file).
    :license: BSD-2-Clause, see LICENSE for details.
"""

from .std.confluence import INVALID_CHARS
from .logger import ConfluenceLogger
from .util import ConfluenceUtil
from docutils import nodes
from sphinx import addnodes
from sphinx.util.images import guess_mimetype
import os

"""
default content type to use if a type cannot be detected for an asset
"""
DEFAULT_CONTENT_TYPE = 'application/octet-stream'

class ConfluenceAsset:
    """
    a confluence asset

    Holds metadata for an asset (image or file).

    Args:
        key: the asset key
        path: the absolute path to the asset
        type: the content type of the asset
        hash: the hash of the asset
    """
    def __init__(self, key, path, type, hash):
        self.docnames = set()
        self.path = path
        self.hash = hash
        self.key = key
        self.type = type

class ConfluenceAssetManager:
    """
    a confluence assets tracker

    The asset manager is used to track detect assets to be referenced to and
    published (if configured) to a Confluence instance. The manager has the
    ability to track locations of assets, detect duplicate uses of assets (when
    references and/or duplicate physical files) and more. Typically, the buidler
    will scan the list of documents to be processed for assets. When the
    translator is running, it will refer to the asset manager to know where an
    asset will be published (so the translator knows how to reference the
    asset). Finally, during the publishing phase, the list of tracked assets can
    be published to the respective publish points.

    Args:
        master: the master document
        env: the build environment
    """
    def __init__(self, master, env):
        self.assets = []
        self.env = env
        self.hash2asset = {}
        self.keys = set()
        self.master = master
        self.path2asset = {}

    def build(self):
        """
        build a list of all assets tracked by the manager

        Returns a list of tuples for all asset entries tracked by this manager.
        A tuple entry will contain the following:

         - The key (or name) of the asset.
         - The absolulte path of the asset on the system.
         - The content-type value of the asset.
         - The hash value of the asset.
         - The name of the document this asset should be published to.

        Returns:
            the list of assets
        """
        data = []
        for asset in self.assets:
            if len(asset.docnames) > 1:
                entry = (asset.key, asset.path, asset.type, asset.hash,
                    self.master)
            else:
                entry = (asset.key, asset.path, asset.type, asset.hash,
                    next(iter(asset.docnames)))
            data.append(entry)
        return data

    def fetch(self, node):
        """
        return key and target document name for provided asset

        When given a asset, cached information will return the name of the
        target document this asset will be published to. In the event an asset
        exists on a single page, the name of that respective page will be
        returned; however, if the asset is found on multiple pages, the master
        document name will be returned instead.

        Args:
            node: the node to interpret

        Returns:
            the key and document name
        """
        docname = None
        key = None

        path = self._interpretAssetPath(node)
        if path:
            asset = self.path2asset.get(path, None)
            if asset:
                key = asset.key

                if len(asset.docnames) > 1:
                    docname = self.master
                else:
                    docname = next(iter(asset.docnames))

        return key, docname

    def process(self, docnames):
        """
        process a list of document for assets

        Given a list of document names, this method will search each document's
        doctree for supported assets which could be published. Asset information
        is tracked in this manager and other helper methods can be used to pull
        asset information when needed.

        Args:
            docnames: the document names to search
        """
        for docname in docnames:
            doctree = self.env.get_doctree(docname)
            self.processDocument(doctree, docname)

    def processDocument(self, doctree, docname, standalone=False):
        """
        process a document for assets

        This method will search each the provided document's doctree for
        supported assets which could be published. Asset information is tracked
        in this manager and other helper methods can be used to pull asset
        information when needed.

        Args:
            doctree: the document's tree
            docname: the document's name
            standalone (optional): ignore hash mappings (defaults to False)
        """
        image_nodes = doctree.traverse(nodes.image)
        for node in image_nodes:
            uri = node['uri']
            if not uri.startswith('data:') and uri.find('://') == -1:
                path = self._interpretAssetPath(node)
                if path not in self.path2asset:
                    hash = ConfluenceUtil.hashAsset(path)
                    type = guess_mimetype(path, default=DEFAULT_CONTENT_TYPE)
                else:
                    hash = self.path2asset[path].hash
                    type = self.path2asset[path].type
                self._handleEntry(path, type, hash, docname, standalone)

        file_nodes = doctree.traverse(addnodes.download_reference)
        for node in file_nodes:
            target = node['reftarget']
            if target.find('://') == -1:
                path = self._interpretAssetPath(node)
                if path not in self.path2asset:
                    hash = ConfluenceUtil.hashAsset(path)
                    type = guess_mimetype(path, default=DEFAULT_CONTENT_TYPE)
                else:
                    hash = self.path2asset[path].hash
                    type = self.path2asset[path].type
                self._handleEntry(path, type, hash, docname, standalone)

    def _handleEntry(self, path, type, hash, docname, standalone=False):
        """
        handle an asset entry

        When an asset is detected in a document, the information about the asset
        is tracked in this manager. When an asset is detected, there are
        considerations to be made. If an asset path has already been registered
        (e.g. an asset used twice), only a single asset entry will be created.
        If an asset matches the hash of another asset, another entry is *not
        created (i.e. a documentation set has duplicate assets; *with the
        exception of when ``standalone`` is set to ``True``). In all cases where
        an asset is detected, the asset reference is updated to track which
        document the asset belongs to.

        Args:
            path: the absolute path to the asset
            type: the content type of the asset
            hash: the hash of the asset
            docname: the document name this asset was found in
            standalone (optional): ignore hash mappings (defaults to False)
        """
        asset = self.path2asset.get(path, None)
        if not asset:
            hash_exists = hash in self.hash2asset
            if not hash_exists or standalone:
                # no asset entry and no hash entry (or standalone); new asset
                key = os.path.basename(path)

                # Confluence does not allow attachments with select characters.
                # Filter out the asset name to a compatible key value.
                for rep in INVALID_CHARS:
                    key = key.replace(rep, '_')

                filename, file_ext = os.path.splitext(key)
                idx = 1
                while key in self.keys:
                    idx += 1
                    key = '{}_{}{}'.format(filename, idx, file_ext)
                self.keys.add(key)

                asset = ConfluenceAsset(key, path, type, hash)
                self.assets.append(asset)
                self.path2asset[path] = asset
                if not hash_exists:
                    self.hash2asset[hash] = asset
            else:
                # duplicate asset detected; build an asset alias
                asset = self.hash2asset[hash]
                self.path2asset[path] = asset
        else:
            assert(self.hash2asset[asset.hash] == asset)

        # track (if not already) that this document uses this asset
        asset.docnames.add(docname)

    def _interpretAssetPath(self, node):
        """
        find an absolute path for a target assert

        Returns the absolute path to an assert. For unsupported asset types,
        this method will return ``None`` values. This method should not be
        invoked on external assets (i.e. URLs).

        Args:
            node: the node to parse

        Returns:
            the absolute path
        """
        path = None
        if isinstance(node, nodes.image):
            # uri's will be relative to documentation root.
            path = node['uri']
        elif isinstance(node, addnodes.download_reference):
            # reftarget will be a reference to the asset with respect to the
            # document (refdoc) holding this reference. Use reftarget and refdoc
            # to find a proper path.
            docdir = os.path.dirname(node['refdoc'])
            path = os.path.join(docdir, node['reftarget'])

        abspath = None
        if path:
            path = os.path.normpath(path)
            abspath = os.path.join(self.env.srcdir, path)

        return abspath
