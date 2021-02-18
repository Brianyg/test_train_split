# -*- coding: utf-8 -*-
"""
splite the datasets to train and test 
@author: gang
"""
import os
#import numpy as np
import shutil
from sklearn.model_selection import train_test_split
import config
class SplitDataset():
    def __init__(self, dataset_dir, saved_dataset_dir, train_ratio=0.7):
        self.dataset_dir = dataset_dir
        self.saved_train_dir = saved_dataset_dir+"/train"
        self.saved_test_dir = saved_dataset_dir+"/test"
        
        self.train_ratio = train_ratio
        
        if not os.path.exists(self.saved_train_dir):
            os.mkdir(self.saved_train_dir)
        if not os.path.exists(self.saved_test_dir):
            os.mkdir(self.saved_test_dir)
    
    def _get_file_path(self,label):
        """
        generate file path of each data from the same folder
        Parameters
        ----------
        label : string
        Returns
        -------
        file_path : list
            list of data of the same type

        """
        file_path = []
        type_file_path = os.path.join(self.dataset_dir,label)
        for file in os.listdir(type_file_path):
            single_file_path = os.path.join(type_file_path,file)
            file_path.append(single_file_path)
        return file_path    

    def _get_label_names(self):
        """
        find labels(types) based on the folder names
        inside each folder there is one type of dataset
        Returns
        -------
        labels : set
            types(categories) of dataset

        """
        labels = set()
        for item in os.listdir(self.dataset_dir):
            item_path = os.path.join(self.dataset_dir,item)
            if os.path.isdir(item_path):
                labels.add(item)
        return labels
    def split_files(self):
        """
        splite the dataset of each label as training dataset and testing dataset
        
        """
        for item in self._get_label_names():
            file_path_list = self._get_file_path(item)
            train_path, test_path = train_test_split(file_path_list,train_size=self.train_ratio)
            self._copy_file(train_path,self.saved_train_dir+"/"+item)
            self._copy_file(test_path,self.saved_test_dir+"/"+item)
    def _copy_file(self,path_list, saved_path):
        """
        copy file from path_list to saved_path

        """
        if not os.path.exists(saved_path):
            os.mkdir(saved_path)
        for path in path_list:
            shutil.copy(path,saved_path)
def create_file(dataset_dir,labels,number_files):
    """
    Generate some dataset for testing
    Parameters
    ----------
    dataset_dir : string
        the directory for the dataset
    labels : list
        list of data labels
    number_files : int
        # of files generated for each type (label)
    Returns
    -------
    None.

    """
    for item in labels:
        saved_dir = os.path.join(dataset_dir,item)
        if not os.path.exists(saved_dir):
            os.mkdir(saved_dir)
        for i in range(number_files):
            file_name = f'{i:03}'
            file_dir = os.path.join(saved_dir,file_name)
            file = open(file_dir,"w")
            file.write(file_name)
            file.close
            
            
if __name__ == '__main__':
    #labels = ["apple","grape","orange"]
    create_file(config.dataset_dir,config.labels,config.number_files)
    split_dataset = SplitDataset(dataset_dir=config.dataset_dir,saved_dataset_dir=config.saved_dataset_dir,train_ratio=config.train_ratio)
    split_dataset.split_files()        
        
