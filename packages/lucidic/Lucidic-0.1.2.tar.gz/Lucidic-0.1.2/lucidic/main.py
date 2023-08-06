##############################################################################
# CloudMage : Lucidic(t)
#====================================================================
# CloudMage Lucidic(t) Python Dictionary Utility Library
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
import copy
import logging

Logger = logging.getLogger('cloudmage.lucidic')

###########################
# Lucidic(t) Class:
###########################
class Lucidic(object):
    """CloudMage Dictionary helper utility Class

    ...

    Private Methods :
    -------
    _get_results() :
        Returns _results list containing search, compare, or other operation _results list object

    _set_results(result) :
        Appends the passed result to the _results list object

    _clear_results() :
        Clears the contents of the _results list object

    _set_search_result(self, keypath, match) :
        Takes a constructed keypath list, and key:value match dict as arguments, and uses them to construct an update that gets appended to the _results list object containing the search match content.

    _construct_list_keypath(keypath, k, list_index) :
        Takes a keypath list, parent dict key and list index as an argument and uses them to construct a concatinated keypath entry that consists of the list item and index number of the requested list item to be added to the search result _result list object.

    _search_item_match(self, key, value, keypath) :
        Takes a dict key string, and value string and keypath list as arguments. The method will evaluate the set search keyword against the key and value, and if a match is found, it will send a constructed result to _set_search_result to append the found occurrence to the _result list object.

    Public Methods :
    -------
    version()
        Returns the semantic version of the Lucidic Library
    """


    def __init__(self, dictionary=None):
        """
        Initialization method that instantiates the Lucidic Dictionary Util class. This class is designed to make common dictionary operations simple. This class library will have the ability to perform tasks such as comparing dictionaries to find differences (added keys, removed keys, value changes, etc), search for keys or values in a nested structure, aid in the creation of a dictionary from a list or delimited string value, and a few other operational simplification methods that are still TBD.
        
        Parameters :
        ------------
        dictionary : {dict: Optional}
            Description : Pass a dictionary that you want to perform any of the class methods on, or use as the base dictionary to compare to another specified dictionary. Original Dictionary is unmodified, as Lucidic will instantiate on a dictionary copy as opposed to the actual dictionary object.
            Default     : If no existing dictionary is passed then a new empty dictionary will be defined.
        
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
            # Use copy.deepcopy to make a true dict copy, dict.copy() will still allow mutable changes to occur in origin.
            self.dict = copy.deepcopy(dictionary)
            Logger.debug('{} specified during the construction of this class instance.'.format(dictionary))
        else:
            self.dict = {}
            Logger.debug("No dictionary was specified during the construction of this class instance. Instance instantiated as a new blank dictionary.")

        # Instantiate Instance Variables that will be used throughout this class.
        '''Search'''
        self._results = []
        self._keyword = str("")
        self._strict = False


    ##############################
    # Getter and Setter Methods: #
    ##############################
    def _get_results(self):
        '''Internal method to get the current value of self._search_results'''
        return self._results


    def _set_results(self, result):
        '''Internal method to set the value of self._results'''
        self._results.append(result)


    def _clear_results(self):
        '''Internal method to clear the contents from self._results'''
        self._results.clear()


    def _get_keyword(self):
        '''Internal method to get the current value of self._keyword'''
        return self._keyword


    def _set_keyword(self, keyword):
        '''Internal method to set the value of self._keyword'''
        
        ThisMethod = inspect.stack()[0][3]
        assert isinstance(keyword, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keyword", "str", keyword, type(keyword))
        
        self._keyword = str(keyword)


    def _clear_keyword(self):
        '''Internal method to clear the value of self._keyword'''
        self._keyword = str("")


    def _get_strict(self):
        '''Internal method to get the current value of self._strict'''
        return self._strict

    
    def _set_strict(self):
        '''Internal method to set the current value of self._strict to True'''
        self._strict = bool(True)


    def _unset_strict(self):
        '''Internal method to set the value of self._strict to False'''
        self._strict = bool(False)


    def _reset_instance(self):
        '''Internal method to remove any previously assigned results, keywords, or strict settings'''
        self._clear_results()
        self._clear_keyword()
        self._unset_strict()


    ############################
    # Internal Search Methods: #
    ############################
    def _set_search_result(self, keypath, match):
        """Sudo private internal class method used to simply update the search results list. This function will take a keypath parameter representing the dictionary path to the searched result, along with a match parameter representing the K:V pair that contains the searched result. The appended result will be a copy of the passed keypath and match as to ensure that the values are not linked to the internal vars, which subsequently get updated. (Bug in pre-release).

        Parameters :
        ------------
        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item.
        
        match : {dict: Required}
            Description : 1 item dictionary containing the {key:value} pair that contains the matched searched result.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        None : 
            This method does not return a value, although it does append the result item to the instance self._search_results list.

        Syntax :
        ------------
            >>> self._set_search_result([keypath], {k: v})
        
        Example :
        ------------
            >>> self._set_search_result(['Customers', 'Address'], {'Name': 'Home'})
        
        Example Result :
        ------------
            >>> [{'keypath': ['Customers', 'Address'], 'match': {'Name': 'Home'}}]
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))
        assert isinstance(match, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "match", "dict", match, type(match))

        # We have to copy the passed list and dict so they are no longer shared with the instance var or all occurrences will be identical and updated when a new key is appended to the list.
        Logger.debug("Adding matched result to the search result list: {}".format({"keypath": keypath.copy(), "match": match.copy()}))
        try:
            search_result = {"keypath": keypath.copy(), "match": match.copy()}
            self._set_results(search_result)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to append search results to self._search_results: {}".format(ThisMethod, str(e)))
            raise e


    @staticmethod
    def _construct_list_keypath(keypath, k, list_index):
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
        
        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        list_item_keypath : {list}
            Description : The return list will contain a keypath list object, containing all keys including list index's of dict keys/list items traversed to the matched result.

        Syntax :
        ------------
            >>> list_keypath = self._construct_list_keypath(keypath, k, v.index(item))
        
        Example :
        ------------
            >>> list_keypath = self._construct_list_keypath(['Customers', 'Address'], "Business", 0)
        
        Example Result :
        ------------
            >>> ['Customers', 'Address', 'Business[0]']
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
            Logger.error("Error occurred in method: {}, attempting to create list_item_keypath value: {}".format(ThisMethod, str(e)))
            raise e

        return list_item_keypath

    def _search_item_match(self, key, value, keypath):
        """Sudo private internal class method used to evaluate the specified keyword against the current item. The item could be a list index that was passed in, or a dict value. The origin dict key is also passed and the keyword is also evaluated against the origin key for a potential match. The method will perform a loose match, as in the evaluation will consist of: [if keyword in key, or if keyword in item]. This will return true if the keyword is a substring within the evaluated value. If `strict` is set to `True`, then the method will perform an exact match search, as in the evaluation will consist of [if keyword == key, or if keyword == item]. When a match is determined this method will call the internal class method self._set_search_result to add the result to the return result list. The 'keyword' and 'strict' values are set as part of the public search method, and are set as self attributes so that they can be accessed by these internal class methods.

        Parameters :
        ------------
        key : {str: Required}
            Description : The key of the origin dictionary, along with the value of the specified key that is being used in the search evaluation.

        value : {str: Required}
            Description : The value being evaluated against the keyword. This could consist of a dict key's value, or a list item.
        
        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._set_search_result.

        Syntax :
        ------------
            >>> self._search_item_match("dictOrListKey", "dictOrListValue", ["keypath"])
        
        Example :
        ------------
            >>> self._search_item_match("Name", "TestDict", ["Record"])
        
        Example Result :
        ------------
            >>> [{'keypath': ["Record"], 'match': {"Name": "TestDict"}}]
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(key, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "key", "str", key, type(key))
        assert not isinstance(value, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "value", "!dict", value, type(value))
        assert not isinstance(value, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "value", "!list", value, type(value))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))

        try:
            # Ensure the search items are strings so that they can be evaluated.
            key = str(key)
            value = str(value)
            keyword = self._get_keyword()
            strict = self._get_strict()

            if (keyword.lower() in key.lower() or keyword.lower() in value.lower()) and (not isinstance(value, dict) or not isinstance(value, list)) and not strict:
                # Log result
                Logger.debug("Loose Match found in evaluated item: {}. Value is of type: {}".format(value, type(value)))
                self._set_search_result(keypath, {key: value})
            # Exact Search, keyword must exactly match the given key or value within the current iteration. This is specified by strict being set to true.
            elif (keyword == key or keyword == value) and (not isinstance(value, dict) or not isinstance(value, list)) and strict:
                # Log result
                Logger.debug("Exact Match found in evaluated item: {}. Value is of type: {}".format(value, type(value)))
                self._set_search_result(keypath, {key: value})
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to search {}:{} for keyword {}: {}".format(ThisMethod, key, value, keyword, str(e)))
            raise e

    
    def _search_recursive_dict(self, dictobj, keypath):
        """Sudo private internal class method used recursively search through the specified dictionary. The method will evaluate the dict key/value for each item in the dict, if the value of a iterated key is another dict object, the method will recursively call itself, adding the current iterations key to the keypath list, and passing the keypath list with the value to another instance of itself. If the value is a list, then the method will call the self._search_recursive_list method that will perform the same function as this method on list objects. This will allow the method to iterate through the dict values until a comparable non dict, non list value is found, at which point the method will call the self._search_item_match method to attempt to match the value to the given search keyword.

        Parameters :
        ------------
        dictobj : {dict: Required}
            Description : The dict that the method will use to recursively check each key/value pair for a keyword occurrance. In the event that the value of a key is another dict object, then the key of this current item will be added to the keypath list, and the value of the current item will be set to dictobj, and passed back to this method recursively.

        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item. If the value of the current key is another dict object, then the key of that object will be added to the keypath list prior to the keypath list being passed back to the method recursively.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._set_search_result.

        Syntax :
        ------------
            >>> self._search_recursive_dict({k:v}, [keypath])
        
        Example :
        ------------
            >>> self._search_recursive_dict({"Key": "Value"}, ['Records'])

        Example Result :
        ------------
            None
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(dictobj, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "dictobj", "dict", dictobj, type(dictobj))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))

        try:
            for k, v in dictobj.items():
                if isinstance(v, dict):
                    dict_keypath = keypath.copy()
                    dict_keypath.append(k)
                    self._search_recursive_dict(v, dict_keypath)
                elif isinstance(v, list):
                    self._search_recursive_list(k, v, keypath)
                else:
                    self._search_item_match(k, v, keypath)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to recursively iterate through: {} in keypath: {} : {}".format(ThisMethod, dictobj, keypath, str(e)))
            raise e


    def _search_recursive_list(self, k, listobj, keypath):
        """Sudo private internal class method used recursively search through the specified list. The method will evaluate each item in the list, if the value of an item is a nested list, the method will recursively call itself, adding the current iterations parent dict key to the keypath list, along with the list item index. and pass the keypath list with the list item to another instance of itself. If the value is a dict, then the method will call the self._search_recursive_dict method that will perform the same function as this method on a nested dict object. This will allow the method to iterate through the list values until a comparable non dict, non list value is found, at which point the method will call the self._search_item_match method to attempt to match the value to the given search keyword.

        Parameters :
        ------------
        k : {str: Required}
            Description : The key of the parent dict of which the value was this or a parent list object.
        
        listobj : {list: Required}
            Description : The list that the method will use to recursively check each item for a keyword occurrance. In the event that the value of the item is another list object, then the key of the parent list, as well as this current item will be added to the keypath list, and the value of the current item will be set to sublist, and passed back to this method recursively.

        keypath : {list: Required}
            Description : List passed into the method containing values for all of the keys that were traversed in order to get to the search result item. If the value of the current key is another dict object, then the key of that object will be added to the keypath list prior to the keypath list being passed back to the method recursively.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.
        
        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        None :
            Description : This method doesn't directly return a value, when a positive match is found, the match is added to the search results list by calling the internal class method self._set_search_result.

        Syntax :
        ------------
            >>> self._search_item_match(dictkey, listobj, [keypath])
        
        Example :
        ------------
            >>> self._search_item_match("Records", [{"Key": "Value}], ['Business'])

        Example Result :
        ------------
            None
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(k, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "k", "str", k, type(k))
        assert isinstance(listobj, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "listobj", "list", listobj, type(listobj))
        assert isinstance(keypath, list), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keypath", "list", keypath, type(keypath))
        
        try:
            for item in listobj:
                if isinstance(item, dict):
                    list_keypath = self._construct_list_keypath(keypath, k, listobj.index(item))
                    self._search_recursive_dict(item, list_keypath)
                elif isinstance(item, list):
                    list_keypath = self._construct_list_keypath(keypath, k, listobj.index(item))
                    prevkey = str(list_keypath[-1:]).replace("['", "").replace("']", "")
                    self._search_recursive_list(prevkey, item, list_keypath)
                else:
                    self._search_item_match("{}[{}]".format(k, listobj.index(item)), item, keypath)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to recursively iterate through: {}:{} in keypath: {} : {}".format(ThisMethod, k, listobj, keypath, str(e)))
            raise e


    def _replace_null_dict_values(self, dictobj, key_replace=None, value_replace=None):
        """Sudo private internal class method that will recursively scan a specified dictionary object and clean out any None, Null or empty string ("") values that are encountered, by setting those discovered values to a default value such as 'Undefined'. This is especially helpful when dealing with AWS DynamoDB, a NoSQL DB that doesn't allow the input of NoneType, Null, Nill, or empty sting valued keys to be stored within it's table structure. When this method is called, the origin dictionary is copied, and all replacement actions are taken on the copy. The original dict structure is not modified in any way.

        Parameters :
        ------------
        dictobj : {str: Required}
            Description : The Python dictionary object that will be recursively searched for None, Null, Nil, or empty string values. If the value of any dict key is another dict object, this method will recursively call itself passing in the new object to the recursive method call.

        keyword : {str: Required}
            Description : The string value that will be set for any keys that currently have values set to None, Null, Nil, or an empty string ("").

        key_replace : {str: Optional}
            Description : String value containing the name of a dict key to look for and replace with the specified keyword. This variable is only used for replaceKey public method.
            Default     : None

        value_replace : {str: Optional}
            Description : String value containing the name of a dict key=>value to look for and replace with the specified keyword. This variable is only used for replaceValue public method.
            Default     : None

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        None :
            Description : This method doesn't return a value, it does however update the passed dict keys, whose values are None, Null, Nil, or empty strings with the defined replacement string set in the public caller replaceNull method.

        Syntax :
        ------------
            >>> self._replace_null_dict_values(dictobj, key_replace="SomeKey", value_replace="SomeValue")
        
        Example :
        ------------
            >>> self._replace_null_dict_values(self.dict)
            >>> self._replace_null_dict_values(self.dict, key_replace="SomeKey")
            >>> self._replace_null_dict_values(self.dict, value_replace="SomeValue")

        Example Result :
        ------------
        None : The passed dict object will be modified via the dict.update() method. An example of change is as follows:
            >>> {'key': ''}
            >>> {'key': 'Undefined'}
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(dictobj, dict), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "dictobj", "dict", dictobj, type(dictobj))
        
        # Check if key_replace or value_replace was passed. These values would only be passed for the calls to the replaceKey or replaceVal public methods. If not then set to None.
        if key_replace is not None:
            assert isinstance(key_replace, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "key_replace", "str", key_replace, type(key_replace))
            key_replace = str(key_replace)
        else:
            key_replace == None
        if value_replace is not None:
            assert isinstance(value_replace, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "value_replace", "str", value_replace, type(value_replace))
            value_replace = str(value_replace)
        else:
            value_replace = None

        # Pull the replace_str value into this method to assign the replacement keyword.
        replace_str = self._get_keyword()

        try:
            # If the key replacement variable is set, then look at the dict keys, and if a key match's then replace it.
            if key_replace is not None and key_replace in dictobj.keys():
                dictobj.update({ replace_str : dictobj.get(key_replace) })
                dictobj.pop(key_replace)

            # Recursively scan through the specified dictionary object and test each value, replacing None, Null, Nil, or empty strings with the replace_str set in the public caller method.
            for k, v in dictobj.items():
                # If the value of the key is a dictionary, then recursively call this method
                if isinstance(v, dict):
                    Logger.debug("Dictionary object detected, recursively calling {} on {}.".format(ThisMethod, v))
                    self._replace_null_dict_values(v, key_replace, value_replace)
                # If the value of the key is a list, then look at each list item, and if the item is a nested dict, then recursively call this method.
                elif isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict):
                            self._replace_null_dict_values(item, key_replace, value_replace)
                # If the value of the current key is None, Null, Nil, or an empty string, redefine it to the specified replace_str value
                elif (v is None or v.lower() == 'null' or v.lower() == "nil" or v == "") and key_replace is None and value_replace is None:
                    Logger.debug("Attribute: {} flagged for value replacement. Resetting current value: {}, to: {}".format(k, v, replace_str))
                    dictobj.update({ k : replace_str })
                
                # If a scrub_val was set, then look for instances of the scrub value and replace it with the replacement value.
                elif value_replace is not None and v == value_replace:
                    Logger.debug("Current value flagged for update. Changeing {}:{} => {}:{}".format(k, v, k, value_replace))
                    dictobj.update({ k : replace_str })
            Logger.debug("All attributes with previous values of None, Null, Nil, or empty strings have been reset to: {}".format(replace_str))
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to reset empty string values in the specified dict object: {}".format(ThisMethod, str(e)))
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

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        {list}
            Description : The return list of dicts will contain keypath, and match results for each match that was found for the keyword against the dict.

        Syntax :
        ------------
            >>> SearchResults = LucidicTest.search("Name")
        
        Example :
        ------------
            >>> LucidicTest = Lucidic(TESTDICT)
            >>> SearchResults = LucidicTest.search("Name")

            >>> LucidicTest2 = Lucidic(TESTDICT)
            >>> SearchResults2 = LucidicTest2.search("Name", strict=True)

        Example Result :
        ------------
        Result {list} :
            >>> [
                    {'keypath': ['Customers'], 'match': {'Name': 'John Doe'}},
                    {'keypath': ['Customers', 'Address'], 'match': {'AliasName': 'Home'}},
                    {'keypath': ['Business[0]'], 'match': {'Name': 'SomeBusiness'}}
                ]
            
            >>> [
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
            '''Method Setup...'''
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing any previously instance cached search results and setting method runtime...")
            
            # Clear previous values from instance vars
            self._reset_instance()

            # Set strict based on if strict was requested by method caller.
            if strict:
                self._set_strict()
            else:
                self._unset_strict()

            # Set Keyword and keypath
            self._set_keyword(keyword)
            keyword = self._get_keyword()
            keypath = []

            # Call the internal _search method to perform the actual search of the given keyword against this class targets dict.
            Logger.debug("Executing search on {} object for occurrences of the keyword: {}, strict flag is set to: {}".format(type(self.dict), keyword, strict))
            if isinstance(self.dict, dict):
                self._search_recursive_dict(self.dict, keypath)
            elif isinstance(self.dict, list):
                self._search_recursive_list("", self.dict, keypath)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to search: {} for keyword: {} using strict: {}: {}".format(ThisMethod, self.dict, keyword, strict, str(e)))
            raise e

        # Return search results
        return self._get_results()


    def replaceNull(self, keyword=None):
        """Public dictionary method that will recursively scan the class instance dictionary object (self.dict) and clean out any None, Null or empty string ("") values that are encountered, by setting those discovered values to a default value such as 'Undefined'. This is especially helpful when dealing with AWS DynamoDB, a NoSQL DB that doesn't allow the input of NoneType, Null, Nill, or empty sting valued keys to be stored within it's table structure. When this object instance was instantiated, the origin dictionary was copied, and all replacement actions are taken on this instance copy (self.dict). The scrub action will be performed on the Instance Class dictionary that was set at the time of this class instance instantiation.

        Parameters :
        ------------
        keyword : {str: Optional}
            Description : The string value that will be used as the replacement for any keys that currently have values set to None, Null, Nil, or an empty string ("").
            Default     : "Undefined"

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        {dict}
            Description : The return object will be a dictionary that is identical to the class instance source dict, with any encountered key values set to None, Null, Nil or an empty string value set to the replacement key word.

        Syntax :
        ------------
            >>> LucidicTest.replaceNull("NullReplacementString")

        Example :
        ------------
            >>> LucidicTest = Lucidic(TESTDICT)
            >>> LucidicTest.replaceNull() # Defaults to 'Undefined'
            >>> DynamoDBRecord = LucidicTest.replaceNull("NullReplacementString")

        Example Result :
        ------------
            >>> {
                    "FirstTierKey1": "FirstTierValue",
                    "FirstTierKey2": "Null",
                    "FirstTierKey3": {
                        "SecondTierKey1": "SomeValue",
                        "SecondTierKey2": "Nil",
                        "SecondTierKey3": "",
                        "SecondTierKey4": {
                            "ThirdTierKey1": "null",
                            "ThirdTierKey2": [
                                { "FourthListTierKey1": "nil" },
                                { "FourthListTierKey2": "" },
                                { "FourthListTierKey3": "FourthListTierValue3" }
                            ]
                        }
                    }
                }
            
            >>> {
                    "FirstTierKey1": "FirstTierValue",
                    "FirstTierKey2": "Undefined",
                    "FirstTierKey3": {
                        "SecondTierKey1": "SomeValue",
                        "SecondTierKey2": "Undefined",
                        "SecondTierKey3": Undefined,
                        "SecondTierKey4": {
                            "ThirdTierKey1": "Undefined",
                            "ThirdTierKey2": [
                                { "FourthListTierKey1": "Undefined" },
                                { "FourthListTierKey2": Undefined },
                                { "FourthListTierKey3": "FourthListTierValue3" }
                            ]
                        }
                    }
                }
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        
        try:
            '''Method Setup...'''
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing any previously instance cached search results and setting method runtime...")
            
            # Clear previous values from instance vars
            self._reset_instance()

            # Set keyword based on if specified by method caller.
            if keyword is not None:
                assert isinstance(keyword, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "keyword", "str", keyword, type(keyword))
                self._set_keyword(keyword)
            else:
                self._set_keyword("Undefined")

            keyword = self._get_keyword()

            # Call the replace_null_dict_values method and return the sanitized dict object back to the method caller.
            self._replace_null_dict_values(self.dict)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to reset empty string values in self.dict object: {}".format(ThisMethod, str(e)))
            raise e

        return self.dict


    def replaceKey(self, key_search, replace_value):
        """Public dictionary method that will recursively scan the class instance dictionary object (self.dict) and replace any found occurrences where the dict key matches the provided dict key given keyword. When this object instance was instantiated, the origin dictionary was copied, and all replacement actions are taken on this instance copy (self.dict). The scrub action will be performed on the Instance Class dictionary that was set at the time of this class instance instantiation.

        Parameters :
        ------------
        key_search : {str: Required}
            Description : Recursively scan the dict for this key name, and when found, rename the key to the provided value set in the 'replace_value' argument.
        
        replace_value : {str: Required}
            Description : The string value that will be used as the replacement for any keys that match the provided key_search. In essence any matched dict key itself will be renamed to this value.

        Raises :
        ------------
        TypeError : 
            Raised if passed variables are not of the properly specified types.

        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        {dict}
            Description : The return object will be a dictionary that is identical to the class instance source dict, with any encountered search_key matched key names renamed to the provided replace_value.

        Syntax :
        ------------
            >>> LucidicTest.replaceKey(key_search, replace_value)
        
        Example :
        ------------
            >>> LucidicTest = Lucidic(TESTDICT)
            >>> LucidicTest.replaceKey("ThirdListTierKey3", "ChangedKey1")
            >>> DynamoDBRecord = LucidicTest.replaceKey("ThirdListTierKey3", "ChangedKey1")

        Example Result :
        ------------
            >>> {
                    "FirstTierKey1": {
                        "SecondTierKey1": "null",
                        "SecondTierKey2": [
                            { "ThirdListTierKey1": "nil" },
                            { "ThirdListTierKey2": "" },
                            { "ThirdListTierKey3": "FourthListTierValue3" }
                        ]
                    }
                }
            
            >>> {
                    "FirstTierKey1": {
                        "SecondTierKey1": "null",
                        "SecondTierKey2": [
                            { "ThirdListTierKey1": "nil" },
                            { "ThirdListTierKey2": "" },
                            { "ChangedKey1": "FourthListTierValue3" }
                        ]
                    }
                }
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        assert isinstance(key_search, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "key_search", "str", key_search, type(key_search))
        assert isinstance(replace_value, str), "{}({}) attribute expected type: {}, however the current value: {} is of type: {}".format(ThisMethod, "replace_value", "str", replace_value, type(replace_value))
        
        try:
            '''Method Setup...'''
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing any previously instance cached search results and setting method runtime...")
            
            # Clear previous values from instance vars
            self._reset_instance()
            self._set_keyword(replace_value)
            keyword = self._get_keyword()

            # Call the replace_null_dict_values method and return the key replaced dict object back to the method caller.
            self._replace_null_dict_values(self.dict, key_replace=key_search)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to rename key: {} to value: {} in self.dict object: {}".format(ThisMethod, key_search, replace_value, str(e)))
            raise e

        return self.dict


    def replaceValue(self, val_search, replace_value):
        """Public dictionary method that will recursively scan the class instance dictionary object (self.dict) and replace any found occurrences where a dict key value matches the provided val_search argument value. When this object instance was instantiated, the origin dictionary was copied, and all replacement actions are taken on this instance copy (self.dict). The scrub action will be performed on the Instance Class dictionary that was set at the time of this class instance instantiation.

        Parameters :
        ------------
        val_search : {str: Required}
            Description : Recursively scan the dict and attempt to match any keys value to the val_search specified in this argument, if found, update the value of the key to the value specified in the 'replace_value' argument.
        
        replace_value : {str: Required}
            Description : The value that will be used as the replacement for any key's value that was matched to the val_search argument value. In essence any matched dict key values will be modified to the value set in this 'replace_value' argument.

        Raises :
        ------------
        GeneralError :
            Raised when method encounters a processing error, that is not otherwise caught.

        Returns :
        ------------
        {dict}
            Description : The return object will be a dictionary that is identical to the class instance source dict, with any encountered key values matching the val_search argument, modified to the provided replace_value value.

        Syntax :
        ------------
            >>> LucidicTest.replaceValue(val_search, replace_value)
        
        Example :
        ------------
            >>> LucidicTest = Lucidic(TESTDICT)
            >>> LucidicTest.replaceValue("ThirdListTierKey3", "ChangedKey1")
            >>> DynamoDBRecord = LucidicTest.replaceValue("FourthListTierValue3", "ChangedValue1")

        Example Result :
        ------------
            >>> {
                    "FirstTierKey1": {
                        "SecondTierKey1": "null",
                        "SecondTierKey2": [
                            { "ThirdListTierKey1": "nil" },
                            { "ThirdListTierKey2": "" },
                            { "ChangedKey1": "FourthListTierValue3" }
                        ]
                    }
                }
            
            >>> {
                    "FirstTierKey1": {
                        "SecondTierKey1": "null",
                        "SecondTierKey2": [
                            { "ThirdListTierKey1": "nil" },
                            { "ThirdListTierKey2": "" },
                            { "ChangedKey1": "ChangedValue1" }
                        ]
                    }
                }
        """
        # Validate the input types are correct
        ThisMethod = inspect.stack()[0][3]
        Logger.debug("Executing Class Method: {}".format(ThisMethod))
        Logger.debug("Validating Lucidic.{} parameters...".format(ThisMethod))
        
        # We are not going to provide assert catch's for key values as values could literally be anything such as sting, int, list, dict, tuple, set, etc.. 
        
        try:
            '''Method Setup...'''
            # Call the internal clear search results method to clear any previous search items in the result list.
            Logger.debug("Clearing any previously instance cached search results and setting method runtime...")
            
            # Clear previous values from instance vars
            self._reset_instance()
            self._set_keyword(replace_value)
            keyword = self._get_keyword()

            # Call the replace_null_dict_values method and return the sanitized dict object back to the method caller.
            self._replace_null_dict_values(self.dict, value_replace=val_search)
        except Exception as e:
            Logger.error("Error occurred in method: {}, attempting to modify the value of {}:{} to {}:{} in self.dict object: {}".format(ThisMethod, k, v, k, replace_value, str(e)))
            raise e

        return self.dict
