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

    Methods
    -------
    version()
        Returns the semantic version of the Lucidic Library
    
    fetch(filepath=None, path=False)
        Split a provided filepath and return back only the filename or path

    Todo
    ----
      - TBD
    """


    def __init__(self, dictionary=None):
        """
        Initialization method that instantiates the Lucidic Dictionary Util class. This class is designed to make common dictionary operations simple. This class library will have the ability to perform tasks such as comparing dictionaries to find differences (added keys, removed keys, value changes, etc), search for keys or values in a nested structure, aid in the creation of a dictionary from a list or delimited string value, and a few other operational simplification methods that are still TBD.
        
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
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        
        if dictionary is not None:
            assert isinstance(dictionary, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "dictionary", "dict", dictionary, type(dictionary))
            self.dict = dictionary
            Logger.debug('{} specified during the construction of this class instance.'.format(dictionary))
        else:
            self.dict = {}
            Logger.debug("No dictionary was specified during the construction of this class instance. Instance instantiated as a new blank dictionary.")


    ############################
    # Internal Search Methods: #
    ############################
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
            >>> self._update_search_results([keypath], {k: v})
            >>> self._update_search_results(['Customers', 'Address'], {'Name': 'Home'})
        
        Example Result :
        ------------
            [{'keypath': ['Customers', 'Address'], 'match': {'Name': 'Home'}}]
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))
        assert isinstance(match, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "match", "dict", match, type(match))

        # We have to copy the passed list and dict so they are no longer shared with the instance var or all occurrences will be identical.
        Logger.debug("Adding matched result to the search result list: {}".format({"keypath": keypath.copy(), "match": match.copy()}))
        self._search_results.append({"keypath": keypath.copy(), "match": match.copy()})


    @staticmethod
    def _search_set_list_keypath(keypath, k, list_index):
        """Sudo private internal static class method used set a temporary keypath in the event that the referenced item is a list index. During the the search, list items are evaluated searching for nested lists or dict values. If the matched item is either, then the search method is recursively called to ensure its able to search through the entire list. During the search method, when a list is encountered, we do not want to update the methods keypath with the index as it will append all subsequently traversed keys to it, so this method serves the purpose of construting a temporarily keypath based on the matched list index so that the keypath for the result
        can be set appropriately within the result set return list.

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

        Example Result :
        ------------
            ['Customers', 'Address', 'Business[0]', 'Address', 'Passcode[0]']
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))
        assert isinstance(k, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "k", "str", k, type(k))
        assert isinstance(list_index, int), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "list_index", "int", list_index, type(list_index))

        try:
            # Copy the keypath list as we want to preserve its current value for the next iteration, and don't want to add a list index to it.
            list_item_keypath = keypath.copy()
            # Construct a unique keypath that includes the list index, so that the the list items can be recursively searched, without altering future iterations.
            list_item_keypath.append("{}[{}]".format(k, list_index))
            Logger.debug("Created new temporary result keypath: {}".format("{}[{}]".format(k, list_index)))
        except Exception as e:
            raise e

        return list_item_keypath

    def _search_item_match(self, key, item2eval, keypath):
        """Sudo private internal class method used to evaluate the specified keyword against the current item. The item could be a list index that was passed in, or a dict value. The origin dict key is also passed and the keyword is also evaluated against the origin key for a potential match. The method will perform a loose match, as in the evaluation will consist of: [if keyword in key, or if keyword in item]. This will return true if the keyword is a substring within the evaluated value. If `strict` is set to `True`, then the method will perform an exact match search, as in the evaluation will consist of [if keyword == key, or if keyword == item]. When a match is determined this method will call the internal class method self._update_search_results to add the result to the return result list. The 'keyword' and 'strict' values are set as part of the public search method, and are set as self attributes so that they can be accessed by these internal class methods.

        Parameters :
        ------------
        key : {str: Required}
            Description : The key of the origin dictionary, along with the value of the specified key that is being used in the search evaluation.

        item2eval : {str: Required}
            Description : The value being evaluated against the keyword. This could consist of a dict key's value, or a list item.
        
        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._update_search_results.

        Example :
        ------------
            >>> self._search_item_match("dictOrListKey", "dictOrListValue", ["keypath"])
            >>> self._search_item_match("Name", "TestDict", ["Record"])
            >>> self._search_item_match("Type", "Name", ["Record"])

        Example Result :
        ------------
            [{'keypath': ["Record"], 'match': {"Name": "TestDict"}}]
            [{'keypath': ["Record"], 'match': {"Type": "Name"}}]
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(key, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "key", "str", key, type(key))
        assert not isinstance(item2eval, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "item2eval", "!dict", item2eval, type(item2eval))
        assert not isinstance(item2eval, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "item2eval", "!list", item2eval, type(item2eval))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))

        try:
            # Ensure the search items are strings so that they can be evaluated.
            key = str(key)
            keyword = str(self._keyword)
            item2eval = str(item2eval)

            if (keyword.lower() in key.lower() or keyword.lower() in item2eval.lower()) and (not isinstance(item2eval, dict) or not isinstance(item2eval, list)) and not self._strict:
                # Log result
                Logger.debug("Loose Match found in evaluated item: {}. Value is of type: {}".format(item2eval, type(item2eval)))
                self._update_search_results(keypath, {key: item2eval})
            # Exact Search, keyword must exactly match the given key or value within the current iteration. This is specified by strict being set to true.
            elif (keyword == key or keyword == item2eval) and (not isinstance(item2eval, dict) or not isinstance(item2eval, list)) and self._strict:
                # Log result
                Logger.debug("Exact Match found in evaluated item: {}. Value is of type: {}".format(item2eval, type(item2eval)))
                self._update_search_results(keypath, {key: item2eval})
        except Exception as e:
            raise e

    
    def _search_recursive_dict(self, subdict, keypath):
        """Sudo private internal class method used recursively search through the specified dictionary. The method will evaluate the dict key/value for each item in the dict, if the value of a iterated key is another dict object, the method will recursively call itself, adding the current iterations key to the keypath list, and passing the keypath list with the value to another instance of itself. If the value is a list, then the method will call the self._search_recursive_list method that will perform the same function as this method on list objects. This will allow the method to iterate through the dict values until a comparable non dict, non list value is found, at which point the method will call the self._search_item_match method to attempt to match the value to the given search keyword.

        Parameters :
        ------------
        subdict : {dict: Required}
            Description : The dict that the method will use to recursively check each key/value pair for a keyword occurrance. In the event that the value of a key is another dict object, then the key of this current item will be added to the keypath list, and the value of the current item will be set to subdict, and passed back to this method recursively.

        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item. If the value of the current key is another dict object, then the key of that object will be added to the keypath list prior to the keypath list being passed back to the method recursively.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._update_search_results.

        Example :
        ------------
            >>> self._search_recursive_dict(dict, ["keypath"])

        Example Result :
        ------------
            None
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(subdict, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "subdict", "dict", subdict, type(subdict))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))

        try:
            for k, v in subdict.items():
                if isinstance(v, dict):
                    dict_keypath = keypath.copy()
                    dict_keypath.append(k)
                    self._search_recursive_dict(v, dict_keypath)
                elif isinstance(v, list):
                    self._search_recursive_list(k, v, keypath)
                else:
                    # print("k:{}, v:{}, keyword:{}, keypath:{}, strict:{}".format(k, v, self._keyword, keypath, self._strict))
                    self._search_item_match(k, v, keypath)
        except Exception as e:
            raise e


    def _search_recursive_list(self, k, sublist, keypath):
        """Sudo private internal class method used recursively search through the specified list. The method will evaluate each item in the list, if the value of an item is a nested list, the method will recursively call itself, adding the current iterations parent dict key to the keypath list, along with the list item index. and pass the keypath list with the list item to another instance of itself. If the value is a dict, then the method will call the self._search_recursive_dict method that will perform the same function as this method on a nested dict object. This will allow the method to iterate through the list values until a comparable non dict, non list value is found, at which point the method will call the self._search_item_match method to attempt to match the value to the given search keyword.

        Parameters :
        ------------
        k : {str: Required}
            Description : The key of the parent dict of which the value was this or a parent list object.
        
        sublist : {list: Required}
            Description : The list that the method will use to recursively check each item for a keyword occurrance. In the event that the value of the item is another list object, then the key of the parent list, as well as this current item will be added to the keypath list, and the value of the current item will be set to sublist, and passed back to this method recursively.

        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item. If the value of the current key is another dict object, then the key of that object will be added to the keypath list prior to the keypath list being passed back to the method recursively.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._update_search_results.

        Example :
        ------------
            >>> self._search_item_match(k, sublist, ["keypath"])

        Example Result :
        ------------
            None
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(k, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "k", "str", k, type(k))
        assert isinstance(sublist, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "sublist", "list", sublist, type(sublist))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))
        
        try:
            for item in sublist:
                if isinstance(item, dict):
                    list_keypath = self._search_set_list_keypath(keypath, k, sublist.index(item))
                    self._search_recursive_dict(item, list_keypath)
                elif isinstance(item, list):
                    list_keypath = self._search_set_list_keypath(keypath, k, sublist.index(item))
                    prevkey = str(list_keypath[-1:]).replace("['", "").replace("']", "")
                    self._search_recursive_list(prevkey, item, list_keypath)
                else:
                    self._search_item_match("{}[{}]".format(k, sublist.index(item)), item, keypath)
        except Exception as e:
            raise e


    #####################
    # Public Methods: #
    #####################
    def search(self, keyword, strict=False):
        """Public dictionary search method designed to perform a search through the class instantiated target dictionary for the specified keywords provided to the method. The method will search though each key/value pair | list item recursively when either a dict or list object is set as a key's value to ensure that all keys and values in the dict are evaluated for match criteria. There is an optional 'strict' flag that will ensure that 
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
            >>> SearchResults = LucidicTest.search("Name")
            
            >>> LucidicTest2 = Lucidic(TESTDICT, strict=True)
            >>> SearchResults2 = LucidicTest2.search("Name")

        Example Result :
        ------------
            [
                {'keypath': ['Customers'], 'match': {'Name': 'John Doe'}},
                {'keypath': ['Customers', 'Address'], 'match': {'AliasName': 'Home'}},
                {'keypath': ['Business[0]'], 'match': {'Name': 'SomeBusiness'}}
            ]
            
            [
                {'keypath': ['Customers'], 'match': {'Name': 'John Doe'}},
                {'keypath': ['Business[0]'], 'match': {'Name': 'SomeBusiness'}}
            ]
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(keyword, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keyword", "str", keyword, type(keyword))
        assert isinstance(strict, bool), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "strict", "bool", strict, type(strict))
        
        try:
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing previous search results...")
            self._search_results = []
            self._keypath = []
            self._keyword = str(keyword)
            self._strict = strict

            # Call the internal _search method to perform the actual search of the given keyword against this class targets dict.
            Logger.debug("Executing search on {} object for occurrences of the keyword: {}, strict flag is set to: {}".format(type(self.dict), keyword, strict))
            if isinstance(self.dict, dict):
                self._search_recursive_dict(self.dict, self._keypath)
            elif isinstance(self.dict, list):
                self._search_recursive_list("", self.dict, self._keypath)
        except Exception as e:
            raise e

        # Return search results.
        return self._search_results