# %%

import os
import sys
import glob
import win32com.client
import shutil 
#https://forum.amibroker.com/t/calling-amibroker-from-python/9575/3

# %%
# xPathDict={}
# xPathDict['db_path']=r"D:\AB_DB\AB_Fund_World"
# xPathDict['data_path']=r"D:\AB_DB\Script_ImportData\Fund_File\AB_*.csv"
# xPathDict['ab_format_path']=r"D:\AB_DB\Script_ImportData\AB-Wizard.format"



# %%
def import_files_to_Amibroker(xPathDict):

    imp_tbl = [
        {'db': xPathDict['db_path'],
        'data': xPathDict['data_path'],
        'format': xPathDict['ab_format_path']},
    ]

    print(imp_tbl)

    # %%
    def ImportDataToAmibroker(ab, lst):

        try: 
            for l in lst:
                print("Loading database {}".format(os.path.split(l['db'])[1]))
                ab.LoadDatabase(l['db'])
                f_lst = sorted(set(glob.glob(l['data'])))
                for f in f_lst:
                    print(f)
                    try:
                        print("Importing datafile {}, using format {}".format(f, l['format']))
                        ab.Import(0, f, l['format'])
                    except e:
                        print("Error importing datafile {}".format(f))

                print("Saving Amibroker")
                ab.RefreshAll()
                ab.SaveDatabase()
                print("Done it Succesfully")
        except Exception as ex:
            raise ex
        return True

    # %%
    oAB = win32com.client.Dispatch("Broker.Application")
    isOK=ImportDataToAmibroker(oAB, imp_tbl)
    print("Terminated")
    oAB.Quit()

    return isOK

# %%


# %%



