from PIL import Image, ExifTags
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QIcon
import gpsutils


# For data storage and manipulation
class CustomModel:
    """
    pixmaps: is a list containing the actual pixmaps loaded from the interface;
    list_model: is a QStandardItemModel from the Qt library used for the side list of the loaded images;
    table_models: is a list of QStandardItemModel, one for every image's exif data to be displayed in the associated table view.
    """
    def __init__(self):
        # list of pictures loaded
        self.pixmaps = list()
        # list of table models created
        self.table_models = list()
        # model for the side list
        self.list_model = QStandardItemModel()

    def _get_exif_data(self, file_name):
        # extracts exif data from 'filename'
        if file_name != '':
            img = Image.open(file_name)
            if img._getexif() is not None:
                exif_data = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
                return exif_data
            else:
                return None
        else:
            print('file_name is empty! : ' + file_name)
            return None

    def append_new_model(self, file_name):
        # create new model populate it and append it to the list
        mod = QStandardItemModel()
        data = self._get_exif_data(file_name)
        if data is not None:
            for k, v in data.items():
                if k is not None and v is not None:

                    if type(k) == bytes:
                        try:
                            k = k.decode('utf-8', errors='replace')
                        except ValueError:
                            k = str('Unable to read this')

                    if k == 'GPSInfo':
                        '''
                        # The following code adds gps data as separate entries of the exif table

                        gps_data = {}
                        data[k] = ''

                        mod.appendRow([QStandardItem(str(k)), QStandardItem(str(v))])

                        for t in v.keys():
                            sub_decoded = ExifTags.GPSTAGS.get(t, t)
                            gps_data[sub_decoded] = v[t]
                            mod.appendRow([QStandardItem(str(sub_decoded)), QStandardItem(str(v[t]))])
                        '''

                        # extracts longitude and latitude and convert the to be inserted in the Google Maps Link
                        lat, lon = gpsutils.get_lat_lon(v)

                        if lat and lon:
                            forgedK = 'Google Maps Link'
                            #forgedV = '<a href="https://www.google.com/maps/search/?api=1&query={},{}">link</a>'.format(lat, lon)
                            forgedV = 'https://www.google.com/maps/search/?api=1&query={},{}'.format(lat, lon)

                            mod.appendRow([QStandardItem(str(forgedK)), QStandardItem(forgedV)])

                    elif type(v) == bytes:
                        try:
                            v = v.decode('utf-8', errors='replace')
                        except ValueError:
                            v = str('Unable to read this')

                    kit = QStandardItem(str(k))
                    vit = QStandardItem(str(v))
                    mod.appendRow([kit, vit])

        self.table_models.append(mod)

    def load_data(self, files):
        # store data in the models
        for file in files:
            pm = QPixmap(file).scaledToWidth(512)
            item = QStandardItem(file.split('/')[-1])
            item.setIcon(QIcon(pm))
            self.list_model.appendRow(item)
            self.pixmaps.append(pm)
            self.append_new_model(file)

    def remove_image(self, index: int):
        # remove the image corresponding to the index from the models
        self.list_model.removeRow(index)
        del self.table_models[index]
        del self.pixmaps[index]
