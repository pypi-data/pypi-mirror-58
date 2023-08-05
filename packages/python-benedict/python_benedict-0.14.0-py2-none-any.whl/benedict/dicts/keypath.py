# -*- coding: utf-8 -*-

from benedict.utils import dict_util

from six import string_types


class KeypathDict(dict):

    def __init__(self, *args, **kwargs):
        """
        Constructs a new instance.
        """
        self._keypath_separator = kwargs.pop('keypath_separator', '.')
        super(KeypathDict, self).__init__(*args, **kwargs)
        self._check_keypath_separator_in_keys(self)

    @property
    def keypath_separator(self):
        return self._keypath_separator

    @keypath_separator.setter
    def keypath_separator(self, value):
        self._keypath_separator = value
        self._check_keypath_separator_in_keys(self)

    def _check_keypath_separator_in_keys(self, d):
        sep = self._keypath_separator
        if not isinstance(d, dict) or not sep:
            return

        def check_key(parent, key, value):
            if key and isinstance(key, string_types) and sep in key:
                raise ValueError(
                    'keys should not contain keypath separator '
                    '\'{}\', found: \'{}\'.'.format(sep, key))
        dict_util.traverse(d, check_key)

    def _goto_keys(self, keys):
        result = (None, None, None, )
        parent = self
        i = 0
        j = len(keys)
        while i < j:
            key = keys[i]
            try:
                if isinstance(parent, (list, tuple, )):
                    index = int(key)
                    value = parent[index]
                    result = (parent, index, value, )
                else:
                    value = parent[key]
                    result = (parent, key, value, )
                parent = value
                i += 1
            except (KeyError, TypeError, ValueError, ):
                result = (None, None, None, )
                break
        return result

    def _list_keys(self, key):
        if isinstance(key, string_types):
            sep = self._keypath_separator
            if sep and sep in key:
                return list(key.split(sep))
            else:
                return [key]
        elif isinstance(key, (list, tuple, )):
            keys = []
            for key_item in key:
                keys += self._list_keys(key_item)
            return keys
        else:
            return [key]

    def __contains__(self, key):
        keys = self._list_keys(key)
        if len(keys) > 1:
            parent, key, _ = self._goto_keys(keys)
            if isinstance(parent, dict) and parent.__contains__(key):
                return True
            elif isinstance(parent, (list, tuple, )):
                try:
                    value = parent[key]
                    return True
                except IndexError:
                    return False
            else:
                return False
        else:
            return super(KeypathDict, self).__contains__(key)

    def __delitem__(self, key):
        keys = self._list_keys(key)
        if len(keys) > 1:
            parent, key, _ = self._goto_keys(keys)
            if isinstance(parent, dict):
                parent.__delitem__(key)
            elif isinstance(parent, (list, tuple, )):
                try:
                    parent.pop(key)
                except IndexError:
                    raise KeyError
            else:
                raise KeyError
        else:
            super(KeypathDict, self).__delitem__(key)

    def __getitem__(self, key):
        keys = self._list_keys(key)
        value = None
        if len(keys) > 1:
            parent, key, _ = self._goto_keys(keys)
            if isinstance(parent, dict):
                return parent.__getitem__(key)
            elif isinstance(parent, (list, tuple, )):
                return parent[key]
            else:
                raise KeyError
        else:
            value = super(KeypathDict, self).__getitem__(key)
        return value

    def __setitem__(self, key, value):
        self._check_keypath_separator_in_keys(value)
        keys = self._list_keys(key)
        if len(keys) > 1:
            i = 0
            j = len(keys)
            item = self
            while i < j:
                key = keys[i]
                if i < (j - 1):
                    if item is self:
                        subitem = super(KeypathDict, self).get(key, None)
                    else:
                        try:
                            index = int(key)
                        except ValueError:
                            index = None
                        if isinstance(item, dict):
                            subitem = item.get(key, None)
                        elif isinstance(item, (list, tuple, )):
                            try:
                                key = int(key)
                                subitem = item[key]
                            except ValueError:
                                subitem = None
                    if not isinstance(subitem, dict) and isinstance(key, string_types):
                        subitem = item[key] = {}
                    elif not isinstance(subitem, (list, tuple, )) and isinstance(key, int):
                        subitem = item[key] = []
                    item = subitem
                else:
                    item[key] = value
                i += 1
        else:
            super(KeypathDict, self).__setitem__(key, value)

    @classmethod
    def fromkeys(cls, sequence, value=None):
        d = cls()
        for key in sequence:
            d[key] = value
        return d

    def get(self, key, default=None):
        keys = self._list_keys(key)
        if len(keys) > 1:
            parent, key, _ = self._goto_keys(keys)
            if isinstance(parent, dict):
                return parent.get(key, default)
            elif isinstance(parent, (list, tuple, )):
                try:
                    return parent[key]
                except IndexError:
                    return default
            else:
                return default
        else:
            return super(KeypathDict, self).get(key, default)

    def pop(self, key, *args, **kwargs):
        if kwargs and 'default' in kwargs:
            default_arg = True
            default = kwargs.get('default', None)
        elif args:
            default_arg = True
            default = args[0]
        else:
            default_arg = False
            default = None
        keys = self._list_keys(key)
        if len(keys) > 1:
            parent, key, _ = self._goto_keys(keys)
            if isinstance(parent, dict):
                if default_arg:
                    return parent.pop(key, default)
                else:
                    return parent.pop(key)
            elif isinstance(parent, (list, tuple, )):
                if default_arg:
                    try:
                        return parent[key]
                    except IndexError:
                        return default
                else:
                    return parent[key]
            else:
                if default_arg:
                    return default
                else:
                    raise KeyError
        else:
            if default_arg:
                return super(KeypathDict, self).pop(key, default)
            else:
                return super(KeypathDict, self).pop(key)

    def set(self, key, value):
        self.__setitem__(key, value)

    def setdefault(self, key, default=None):
        if key not in self:
            self.__setitem__(key, default)
            return default
        else:
            return self.__getitem__(key)

    def update(self, other):
        self._check_keypath_separator_in_keys(other)
        super(KeypathDict, self).update(other)
