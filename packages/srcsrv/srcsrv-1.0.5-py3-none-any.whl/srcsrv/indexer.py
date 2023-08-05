'''Indexer class
'''
# Python modules
import os
import git
import argparse
# Source index modules
from . import pdb
from . import base


class Indexer(base.Base):
    '''Source indexer class
    '''
    def __init__(self, args):
        super(Indexer, self).__init__(args)

        self._sources = None
        if not args.build_base.endswith('\\'):
            self.args.build_base = args.build_base + '\\'
            
        try:
            if not self.args.hexsha or len(self.args.hexsha) != 40:
                raise ValueError
            int(self.args.hexsha, 16)
        except ValueError:
            self.repo = git.Repo(self.args.build_base)
            self.args.hexsha = self.repo.active_branch.object.hexsha
            self.tree = self.repo.tree()

    @property
    def sources(self):
        '''Create a list of all source files in the repository
        '''
        if not self._sources:
            if self.args.hexsha:
                # If the repo hash was provided we don't prcess the repo tree
                class SourceDict:
                    def __init__(self, args):
                        self.sources = {}
                        self.args = args

                    def __getitem__(self, key):
                        try:
                            return self.sources[key]
                        except KeyError:
                            class Blob:
                                def __init__(self, args, key):
                                    self.path = key[len(args.build_base):].replace('\\', '/')

                            self.sources.update({ key: Blob(self.args, key) })
                            return self.sources[key]
                self._sources = SourceDict(self.args)
            else:
                self._sources = {}
                self._sources_tree(self.tree.trees)
        return self._sources

    def _sources_tree(self, trees):
        '''Private method to recursively process source tree
        '''
        for tree in trees:
            for blob in tree.blobs:
                self._sources.update({ blob.abspath.lower(): blob })
            # traverse tree
            if len(tree.trees):
                self._sources_tree(tree.trees)

        self.tree = self.repo.tree()

    @property
    def sources(self):
        '''Create a list of all source files in the repository
        '''
        if not self._sources:
            self._sources = {}
            self._sources_tree(self.tree.trees)
        return self._sources

    def _sources_tree(self, trees):
        '''Private method to recursively process source tree
        '''
        for tree in trees:
            for blob in tree.blobs:
                self._sources.update({blob.abspath.lower(): (tree.name, blob)})
            # traverse tree
            if len(tree.trees):
                self._sources_tree(tree.trees)

    def _index(self):
        ''' Initial indexing during build
        '''
        for bld_dir in self.args.pdbs:
            bld_dir = os.path.join(self.args.build_base, bld_dir)
            if not os.path.isdir(bld_dir):
                self.logger.error('Directory: {bld_dir} not found')
                continue    # Non-fatal error, skip invalid directory

            for dir, subdirs, files in os.walk(bld_dir):
                for fname in files:
                    if fname.endswith('.pdb'):
                        self.args.pdb = os.path.join(dir, fname)
                        self.args.output = argparse.FileType('w')(self.args.pdb[:-4] + '.ini')
                        pdb.PDB(self).process()

    def _reindex(self):
        ''' @TODO: Process .PDB files after build. This assumes that there's a
                   way to tie back the symbols to the original repo commit hash.
        '''
        pass

    def process(self):
        ''' Process each of the .PDBs
        '''
        if not self.args.pdbs:
            return pdb.PDB(self).process()

        if self.args.action == 1:
            self._index()
        else:
            self._reindex()


__all__ = ['Indexer']
