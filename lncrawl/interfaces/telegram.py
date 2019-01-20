#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from ..utils.user_interface import UserInterface

logger = logging.getLogger('TELEGRAM_BOT')


class TelegramInterface(UserInterface):
    def __init__(self, *args, **kwargs):
        logger.info('Initialized telegram interface')
    # end def

    def get_novel_url(self):
        '''Returns a novel page url or a query'''
        # TODO: must be implemented
        pass
    # end def

    def get_crawlers_to_search(self, links):
        '''Returns user choice to search the choosen sites for a novel'''
        # TODO: must be implemented
        pass
    # end def

    def choose_a_novel(self, search_results):
        '''Choose a single novel url from the search result'''
        # The search_results is an array of (novel_title, novel_url).
        # This method should return a single novel_url only
        #
        # By default, returns the first search_results. Implemented it to
        # handle multiple search_results
        pass
    # end def

    def get_output_path(self, suggested_path):
        '''Returns a valid output path where the files are stored'''
        # You should return a valid absolute path. The parameter suggested_path
        # is valid but not gurranteed to exists.
        #
        # NOTE: If you do not want to use any pre-downloaded files, remove all
        #       contents inside of your selected output directory.
        #
        # By default, returns a valid existing path from suggested_path
        pass
    # end def

    def get_login_info(self):
        '''Returns the (email, password) pair for login'''
        # By default, returns None to skip login
        pass
    # end if

    def get_range_selection(self, chapter_count, volume_count):
        '''Returns a choice of how to select the range of chapters to downloads'''
        # TODO: must be implemented
        # Should return a key from `self.selections` array
        pass
    # end def

    def get_range_using_urls(self, crawler):
        '''Returns a range of chapters using start and end urls as input'''
        # TODO: must be implemented
        # Should return a list of chapters to download
        pass
    # end def

    def get_range_using_index(self, chapter_count):
        '''Returns a range selected using chapter indices'''
        # TODO: must be implemented
        # Should return a list of chapters to download
        pass
    # end def

    def get_range_from_volumes(self, volumes, times=0):
        '''Returns a range created using volume list'''
        # TODO: must be implemented
        # Should return a list of chapters to download
        pass
    # end def

    def get_range_from_chapters(self, crawler, times=0):
        '''Returns a range created using individual chapters'''
        # TODO: must be implemented
        # Should return a list of chapters to download
        pass
    # end def

    def should_pack_by_volume(self):
        '''Returns whether to generate single or multiple files by volumes'''
        # By default, returns False to generate a single file
        pass
    # end def

    def should_fetch_kindlegen(self):
        '''Whether to fetch kindlegen if it does not exists'''
        # By default, returns True to download kindlegen in the user directory to use it
        pass
    # end def
# end class
