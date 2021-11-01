
import yaml

class OperationYaml:

    def __init__(self,path):
        # if path == None:
        #     path = '../../../config/locator.yaml'
        with open(path) as f:
            self.data = yaml.load(f,Loader=yaml.FullLoader)


    def get_locator(self,page,name):

        return self.data[page][name]