import numpy as np
import time

from waggle.plugin import Plugin
from waggle.data.vision import Camera

def compute_mean_color(image):
    return np.mean(image, (0, 1)).astype(float)

def compute_min_color(image):
    return np.min(image, (0,1)).astype(float)

def compute_max_color(image):
    return np.max(image, (0,1)).astype(float)


def main():
    with Plugin() as plugin:
        # open camera and take snapshot
        with Camera("rtsp://admin:Sysadmin25!!@10.107.0.233:10007/h264Preview_01_main") as camera:
            snapshot = camera.snapshot()

        # compute mean color
        mean_color = compute_mean_color(snapshot.data)
        min_color = compute_min_color(snapshot.data)
        max_color = compute_max_color(snapshot.data)

        # publish mean color
        plugin.publish("color.mean.r", mean_color[0], timestamp=snapshot.timestamp)
        plugin.publish("color.mean.g", mean_color[1], timestamp=snapshot.timestamp)
        plugin.publish("color.mean.b", mean_color[2], timestamp=snapshot.timestamp)

        plugin.publish("color.min.r", min_color[0], timestamp=snapshot.timestamp)
        plugin.publish("color.min.g", min_color[1], timestamp=snapshot.timestamp)
        plugin.publish("color.min.b", min_color[2], timestamp=snapshot.timestamp)

        plugin.publish("color.max.r", max_color[0], timestamp=snapshot.timestamp)
        plugin.publish("color.max.g", max_color[1], timestamp=snapshot.timestamp)
        plugin.publish("color.max.b", max_color[2], timestamp=snapshot.timestamp)

        # save and upload image
        snapshot.save("snapshot.jpg")
        plugin.upload_file("snapshot.jpg", timestamp=snapshot.timestamp)

        time.sleep(30)

if __name__ == "__main__":
    main()