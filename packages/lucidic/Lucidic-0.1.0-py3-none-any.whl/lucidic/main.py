##############################################################################
# CloudMage : Lucidic
#====================================================================
# CloudMage Lucid Python Dictionary Utility
#
# Author: Richard Nason rnason@cloudmage.io
# Project Start: 12/23/2019
# License: GNU GPLv3
##############################################################################

###############
# Imports:
###############
import json
import inspect
import logging

Logger = logging.getLogger('cloudmage.lucidic')

###########################
# DictSync() Class:
###########################
class Lucidic(object):
    """CloudMage Dictionary helper utility Class

    ...

    Attributes
    ----------
    command_output : {str}
        The final output of the command back to the user
    filepath : {str}
        The full path to a file such as /var/lib/another/folder/file.ext
    path : {bool}
        Flag to indicate the return the path instead of the filename from the provided input (default false)

    Methods
    -------
    version()
        Returns the semantic version of clarify
    fetch(filepath=None, path=False)
        Split a provided filepath and return back only the filename or path

    Todo
    ----
      - TBD
    """


    def __init__(self, dictionary=None):
        """
        Initialization method that instantiates the Dictionary Sync class. This class is designed to make common dictionary operations simple. This class library will have the ability to perform tasks such as comparing dictionaries to find differences (added keys, removed keys, value changes, etc), search for keys or values in a nested structure, aid in the creation of a dictionary from a list or delimited string value, and a few other operational simplification methods that are still TBD.
        
        Parameters :
        ------------
        dictionary : {dict: Optional}
            Description : Pass a dictionary that you want to perform any of the class methods on, or use as the base dictionary to compare to another specified dictionary.
            Default     : If no dictionary is passed then a new dictionary will be defined.
        
        Attributes :
        ------------
        self.dict : {dict}
            Description : The instantiation target of this class. DictObj = Lucidic(TESTDICT) where TESTDICT is a python dictionary.
            Default     : {}
        """
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        
        if dictionary is not None:
            assert isinstance(dictionary, dict), self._error(TypeError("Method attribute expected type dict, but received type: {}".format(type(dictionary))))
            self.dict = dictionary
            Logger.debug('{} was the dictionary specified during the construction of this class instance.'.format(dictionary))
        else:
            self.dict = {}
            Logger.debug("No dictionary was specified during the construction of this class instance. Instance instantiated as a new blank dictionary.")

        # Set a class instance variable that will hold search results for various dictionary searches.
        self._search_results = []


    #####################
    # Internal Methods: #
    #####################
    def _clear_search_results(self):
        """Sudo private internal class method used to simply clear the class instance search results list
        Calling this method will clear the list and reset the var to []

        Parameters, Raises, Returns :
        ------------
        None

        Examples :
        ------------
            self._clear_search_results()
        """
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        Logger.debug("Clearing previous search results...")
        self._search_results.clear()


    def _update_search_results(self, keypath, match):
        """Sudo private internal class method used to simply update the search results list. This function
        will take a keypath parameter representing the dictionary path to the searched result, along with a
        match parameter representing the K:V pair that contains the searched result. The appended result will be
        a copy of the passed keypath and match as to ensure that the values are not linked to the internal vars,
        which subsequently get updated. (Bug in pre-release).

        Parameters :
        ------------
        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item.
        
        match : {dict: Required}
            Description : Dictionary representing the {key:value} pair that contains the matched searched result.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        None : 
            This method does not return a value, although it does append the result item to the instance self._search_results list.

        Example :
        ------------
            >>> self._update_search_results(keypath, {k: v})
        
        Example Result :
        ------------
            [{'keypath': ['Customers', 'Address'], 'match': {'Name': 'Home'}}]
        """
        # Validate the input types are correct
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        Logger.debug("Validating method parameters...")
        assert isinstance(keypath, list), self._error(TypeError("Method attribute expected type list, but received type: {}".format(type(keypath))))
        assert isinstance(match, dict), self._error(TypeError("Method attribute expected type dict, but received type: {}".format(type(match))))
        
        # We have to copy the passed list and dict so they are no longer shared with the instance var or all occurrences will be identical.
        Logger.debug("Adding matched result to the search result list: {}".format({"keypath": keypath.copy(), "match": match.copy()}))
        self._search_results.append({"keypath": keypath.copy(), "match": match.copy()})

    
    @staticmethod
    def _search_set_list_keypath(keypath, k, list_index):
        """Sudo private internal static class method used set a temporary keypath in the event that the referenced item is a list index.
        During the the search, list items are evaluated searching for nested lists or dict values. If the matched item is either, then the
        search method is recursively called to ensure its able to search through the entire list. During the search method, when a list is
        encountered, we do not want to update the methods keypath with the index as it will append all subsequently traversed keys to it, so
        this method serves the purpose of construting a temporarily keypath based on the matched list index so that the keypath for the result
        can be set appropriately.

        Parameters :
        ------------
        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item.

        k : {str: Required}
            Description : The key of the current dictionary iteration whose value contains the list object.
        
        list_index : {int: Required}
            Description : The index of the list item that contains the nested dict or list object, which needs to be recursively sent back through the search method.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        list_item_keypath : {list}
            Description : The return list will contain a keypath list object, containing all keys including list index's of dict keys/list items traversed to the matched result.

        Example :
        ------------
            >>> list_keypath = self._search_set_list_keypath(keypath, k, v.index(item))
            >>> self._search(item, keyword, list_keypath, strict)

        Example Result :
        ------------
            [
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[1]'], 'match': {'Name': '54321'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[2]'], 'match': {'Name': '34512'}}
            ]
        """
        # Validate the input types are correct
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        Logger.debug("Validating method parameters...")
        assert isinstance(keypath, list), self._error(TypeError("Method attribute expected type list, but received type: {}".format(type(keypath))))
        assert isinstance(k, str), self._error(TypeError("Method attribute expected type str, but received type: {}".format(type(k))))
        assert isinstance(list_index, int), self._error(TypeError("Method attribute expected type int, but received type: {}".format(type(list_index))))
        
        try:
            # Copy the keypath list as we want to preserve its current value for the next iteration, and don't want to add a list index to it.
            list_item_keypath = keypath.copy()
            # Construct a unique keypath that includes the list index, so that the the list items can be recursively searched, without altering future iterations.
            list_item_keypath.append("{}[{}]".format(k, list_index))
            Logger.debug("Created new temporary result keypath: {}".format("{}[{}]".format(k, list_index)))
        except Exception as e:
            raise e

        return list_item_keypath

    
        
    def _search(self, dictobj, keyword, keypath, strict=False):
        """Sudo private internal class method used to perform the actual search through the target dictionary for the specified keywords provided
        to the method. The method will search though each key/value pair recursively when either a dict or list object is set as a key's value to
        ensure that all keys and values in the dict are evaluated for match criteria. There is an optional 'strict' flag that will ensure that 
        matches are not like matches as in if 'keyword' in 'value', but instead an exact match as in if 'keyword' == 'value'. This method is called
        from the public search method, and the return is the self._search_results list that is maintained and managed by 2 other private methods.

        Parameters :
        ------------
        dictobj : {dict: Required}
            Description : The dictionary to be searched for the given keyword. When called by the public search method, the target dictionary is the class instance, self.dict.

        keyword : {str: Required}
            Description : The given keyword that will be used as a match target to find results in the specified dictionary.
        
        keypath : {list: Required}
            Description : List of all dict keys and list index's traversed to find the currently selected keyword match from the dictionary search.

        strict : {bool: Optional}
            Description : Bool flag passed at the time of calling the public search method. Default value is set to False, which will instruct the search to perform a loose search.
                          This means that the search criteria will be a if keyword in value, looking for substrings within the key or value its compared to. Setting the strict flag
                          to True, will instead demand an exact match as in if keyword == value. This will limit results, as match's have to be exact.
            Default     : False 

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        self._search_results : {list}
            Description : The return list of dicts will contain keypath, and match results for each match that was found for the keyword against the dict.

        Example :
        ------------
            >>> self._search(self.dict, keyword, self._keypath, strict)

        Example Result :
        ------------
            [
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[1]'], 'match': {'Name': '54321'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[2]'], 'match': {'Name': '34512'}}
            ]
        """
        # Validate the input types are correct
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        Logger.debug("Validating method parameters...")
        assert isinstance(dictobj, dict), self._error(TypeError("Method attribute expected type dict, but received type: {}".format(type(dictobj))))
        assert isinstance(keyword, str), self._error(TypeError("Method attribute expected type str, but received type: {}".format(type(keyword))))
        assert isinstance(keypath, list), self._error(TypeError("Method attribute expected type list, but received type: {}".format(type(keypath))))
        assert isinstance(strict, bool), self._error(TypeError("Method attribute expected type bool, but received type: {}".format(type(strict))))

        try:
            Logger.debug("Search initiated for keyword: {}, strict flag is set to: {}".format(keyword, strict))
            # For each key/value in the dictionary:
            for k, v in dictobj.items():
                Logger.debug("Searching for keyword occurrences in key: {}".format(k))
                Logger.debug("Searching for keyword occurrences in value: {}".format(v))
                # Check loose match for keyword occurrences within either the current key or value iteration.
                # If the value is a dict, or list, then condition will fail, and push to else bracket where lists and dict values are handled.
                # If strict is enabled, then this loose search condition will also fail, forcing the exact match search next. 
                if (keyword.lower() in k.lower() or keyword.lower() in str(v).lower()) and not isinstance(v, dict) and not isinstance(v, list) and not strict:
                    # Log result
                    Logger.debug("Loose Match found in either this iterations Key: {} or Value: {}. Value is of type: {}".format(k, v, type(v)))
                    self._update_search_results(keypath, {k: v})
                # Exact Search, keyword must exactly match the given key or value within the current iteration. This is specified by strict being set to true.
                if (keyword == k or keyword == v) and strict:
                    # Log result
                    Logger.debug("Exact Match found in either this iterations Key: {} or Value: {}. Value is of type: {}".format(k, v, type(v)))
                    self._update_search_results(keypath, {k: v})
                else:
                    # If the value is a dict, then set the current key within the keypath and recursively call this method.
                    if isinstance(v, dict):
                        Logger.debug("Current value contains dict, calling method recursively against the value obj: {}".format(v))
                        keypath.append(k)
                        self._search(v, keyword, keypath, strict)
                    # If the value is a list, then for each item in the list, evaluate if the list contains any dicts, and if so, set a temp keypath with the list item index
                    # and recursively call this method to parse the nested dict object.
                    elif isinstance(v, list):
                        Logger.debug("Current value contains list, calling method recursively against the value obj: {}".format(v))
                        for item in v:
                            if isinstance(item, dict):
                                Logger.debug("Current list item contains dict, calling method recursively against the value obj: {}".format(item))
                                # Get temp keypath with set list index.
                                list_keypath = self._search_set_list_keypath(keypath, k, v.index(item))
                                Logger.debug("Temporary keypath value assigned for list result: {}".format(list_keypath))
                                self._search(item, keyword, list_keypath, strict)
        except Exception as e:
            raise e

        return self._search_results


    #####################
    # Public Methods: #
    #####################
    def search(self, keyword, strict=False):
        """Public dictionary search method designed to perform a search through the class instantiated target dictionary for the specified keywords provided
        to the method. The method will search though each key/value pair recursively when either a dict or list object is set as a key's value to
        ensure that all keys and values in the dict are evaluated for match criteria. There is an optional 'strict' flag that will ensure that 
        matches are not like matches as in if 'keyword' in 'value', but instead an exact match as in if 'keyword' == 'value'.

        Parameters :
        ------------
        keyword : {str: Required}
            Description : The given keyword that will be used as a match target to find results in the specified dictionary.

        strict : {bool: Optional}
            Description : Bool flag passed at the time of calling the public search method. Default value is set to False, which will instruct the search to perform a loose search.
                          This means that the search criteria will be a if keyword in value, looking for substrings within the key or value its compared to. Setting the strict flag
                          to True, will instead demand an exact match as in if keyword == value. This will limit results, as match's have to be exact.
            Default     : False 

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        {list}
            Description : The return list of dicts will contain keypath, and match results for each match that was found for the keyword against the dict.

        Example :
        ------------
            >>> LucidicTest = Lucidic(TESTDICT)
            >>> LucidicTest2 = Lucidic(TESTDICT, strict=True)
            >>> SearchResults = LucidicTest.search("Name")

        Example Result :
        ------------
            [
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[0]'], 'match': {'Name': '12345'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[1]'], 'match': {'Name': '54321'}}
                {'keypath': ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[2]'], 'match': {'Name': '34512'}}
            ]
        """
        # Validate the input types are correct
        Logger.debug("Executing Class Method: {}".format(inspect.stack()[0][3]))
        Logger.debug("Validating method parameters...")
        assert isinstance(keyword, str), self._error(TypeError("Method attribute expected type str, but received type: {}".format(type(keyword))))
        assert isinstance(strict, bool), self._error(TypeError("Method attribute expected type bool, but received type: {}".format(type(strict))))
        
        try:
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing previous search results...")
            self._clear_search_results()
            self._keypath = []

            # Call the internal _search method to perform the actual search of the given keyword against this class targets dict.
            Logger.debug("Executing search on this dict object for occurrences of the keyword: {}, strict flag is set to: {}".format(keyword, strict))
            self._search(self.dict, keyword, self._keypath, strict)
        except Exception as e:
            raise e

        # Return search results.
        return self._search_results