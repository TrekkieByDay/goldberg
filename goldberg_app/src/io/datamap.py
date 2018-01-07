# Python imports
import warnings

# Local imports

# Third party imports
import numpy as np
import pandas as pd
import numpy as np

class Catagories():

    _TAG = "CAT_"

    def __init__(self, **flags):
        for key, val in flags.items():
            if not isinstance(val, bool):
                raise TypeError('Catagories class fields must be of type bool')
            object.__setattr__(self, key, val)

class Member:

    _CODE_TAG = "py-"

    def __init__(self, args=None, name=None, val=None, types_allowed=None, type_cast=None,
                 vals_allowed=None, test=None, key=None):
        self.name = name
        self.val = val
        self.types_allowed = types_allowed
        self.type_cast = type_cast
        self.vals_allowed = vals_allowed
        self.test = test
        self.key = key
        self.cats = None

        if args is not None:
            for k, v in self.__dict__.items():
                val = args.get(k, None)
                if isinstance(val, str) and Member._CODE_TAG in val:
                    try:
                        val = eval(val.split(Member._CODE_TAG)[-1])
                    except:
                        warnings.warn("Failed to eval member value: {%s: %s}" % (k, v))
                object.__setattr__(self, k, val)


            cats = {}
            for k, v in args.items():
                if Catagories._TAG in k:
                    cats[k.split(Catagories._TAG)[-1]] = v
            self.cats = Catagories(**cats)


class Datamap:

    class Members:
        def __init__(self):
            pass

    _SHEET_NAME = "TEMPLATE"
    _EXCEL_EXT = ".xlsx"

    def __init__(self, template=None):

        if template is None:
            raise ValueError('Template file required')
        elif type(template) is not str:
            raise TypeError('Template must be filename str')

        if not template.endswith(Datamap._EXCEL_EXT):
            raise NotImplementedError('Template file must be Excel')

        self.members = Datamap.Members()

        self._load_template_xlsx(template)
        print('stop')



    def _load_template_xlsx(self, template_xlsx):

        # Open Excel file and get DataFrame as dictionary. Transpose is
        # required because of Panda's default orientation
        xl = pd.ExcelFile(template_xlsx)
        df = xl.parse(Datamap._SHEET_NAME)
        xl.close()
        for index, row in df.iterrows():
            mem = Member(args=row)
            setattr(self.members, mem.name, mem)
