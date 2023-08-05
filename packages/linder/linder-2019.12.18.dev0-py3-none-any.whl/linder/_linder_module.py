from .task_util import other_tasks
from .other_util import download_data, save_images
from .predict_util import predict_image
from .fraction_util import calculate_fraction
import numpy as np


def get_land_cover(
    lat_left_top_t,
    lon_left_top_t,
    lat_right_bot_t,
    lon_right_bot_t,
    s_date,
    e_date,
    path_GUF,
    path_data_building,
    path_save,
    download_img=True,
):
    # download_img = settings[cname]["downloading_img"] == "yes"
    # s_date = settings[cname]["s_date"]
    # e_date = settings[cname]["e_date"]

    # [lat_left_top_t, lon_left_top_t] = settings[cname]["coord_top"]
    # [lat_right_bot_t, lon_right_bot_t] = settings[cname]["coord_bot"]

    size = 10  # display parameter. Do not change
    scale = abs(lat_left_top_t - lat_right_bot_t) / abs(lon_left_top_t - lon_right_bot_t


    # path_GUF = settings[cname]["GUF_data"] == "yes"

    Building_data = settings[cname]["building_data"]
    Road_data = settings[cname]["road_data"]
    # if Building_data == "MICROSOFT":
    #     path_data_building = settings[cname]["building_dir"]
    # else:
    #     path_data_building = ""

    # list_of_GUF = sorted(glob("./Data/GUF/WSF2015_v1_EPSG4326/WSF2015_v1_EPSG4326/*"))
    list_of_GUF = list(path_GUF.glob("*tif"))

    # path_save = cname
    all_lats = np.linspace(lat_right_bot_t, lat_left_top_t, num=ny + 1)
    all_lons = np.linspace(lon_left_top_t, lon_right_bot_t, num=nx + 1)
    patch_n = 0
    for i in range(0, len(all_lons) - 1):
        lon_left_top, lon_right_bot = [all_lons[i], all_lons[i + 1]]
        for j in range(0, len(all_lats) - 1):

            skip_patch = input("Skip patch " + str(patch_n) + "? (y/n):")
            while skip_patch not in ["y", "n"]:
                skip_patch = input("Skip patch " + str(patch_n) + "? (y/n):")

            if skip_patch != "y":
                lat_right_bot, lat_left_top = [all_lats[j], all_lats[j + 1]]

                coords_top = [lat_left_top, lon_left_top]
                coords_bot = [lat_right_bot, lon_right_bot]

                download_data(
                    path_save,
                    coords_top,
                    coords_bot,
                    patch_n,
                    s_date,
                    e_date,
                    download_img,
                )
                save_images(path_save, patch_n, scale)
                predict_image(path_save, patch_n, scale)
                other_tasks(
                    path_save,
                    patch_n,
                    path_GUF,
                    Building_data,
                    Road_data,
                    path_data_building,
                    list_of_GUF,
                    lat_left_top,
                    lon_left_top,
                    lat_right_bot,
                    lon_right_bot,
                )

                calculate_fraction(path_save, patch_n, xn, yn)
            patch_n = patch_n + 1
