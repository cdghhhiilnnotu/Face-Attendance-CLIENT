from .hau_importer import *

class DatasetSupport():    
    def reset_path(path_name, remake=True):
        if os.path.exists(path_name):
            shutil.rmtree(path_name)
        if remake:
            os.mkdir(path_name)
    
    def download_datasets_by_class_id(class_id, datasets_path, collector):
        DatasetSupport.reset_path(datasets_path)
        list_msv = collector.get_msv_by_malop(class_id)
        
        students = []
        for msv in list_msv:
            students.append(collector.get_sv_by_msv(msv))

        student_links = []
        for s in students:
            student_links.append(s['LinkAnh'])
        
        current_dir = os.getcwd()
        os.chdir(datasets_path)
        for down_url in student_links:
            os.system(f'gdown --folder --no-cookies {down_url}')
        os.chdir(current_dir)
