# standard libraries
import gettext

from nion.segmentation.stemsegmentation import segmentationSTEM

_ = gettext.gettext



class SampleMenuItemDelegate:

    def __init__(self, api):
        self.__api = api
        self.menu_id = "segmentation_menu"  # required, specify menu_id where this item will go
        self.menu_name = _("Segmentation")  # optional, specify default name if not a standard menu
        self.menu_before_id = "window_menu"  # optional, specify before menu_id if not a standard menu
        self.menu_item_name = _("Real-space segmentation")  # menu item name

    def menu_item_execute(self, window):
        image = window.target_data_item.data
        patch_x = 11             # height of patch
        patch_y = 5              # width of patch
        window_x = 21            # height of window
        window_y = 11            # width of widdow
        n_clusters = 4           # number of the patterns to be segmented
        max_num_points = 100     # maximum number of points to be chosen uniformly 
                                 # from the local correlation map.
                                 # the densest uniform grids will be set up according to this number.
        seg = segmentationSTEM( n_patterns=n_clusters,
                       patch_x=patch_x,patch_y=patch_y,
                       window_x=window_x,window_y=window_y,max_num_points=max_num_points)
        labels = seg.perform_clustering(image)
        api = self.__api
        data_item = api.library.create_data_item_from_data(labels) 
        window.display_data_item(data_item)

class MenuSampleExtension:

    # required for Swift to recognize this as an extension class.
    extension_id = "extension.segmentation"

    def __init__(self, api_broker):
        # grab the api object.
        api = api_broker.get_api(version="~1.0")
        # be sure to keep a reference or it will be closed immediately.
        self.__menu_item_ref = api.create_menu_item(SampleMenuItemDelegate(api))

    def close(self):
        self.__menu_item_ref.close()
        self.__menu_item_ref = None
