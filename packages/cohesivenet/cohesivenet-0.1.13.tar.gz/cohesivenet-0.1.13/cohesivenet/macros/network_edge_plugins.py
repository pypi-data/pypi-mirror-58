import time

from cohesivenet import CohesiveSDKException


def wait_for_images_ready(client, import_uuids=None, interval=1.0, timeout=120.0):
    """Wait for images to be Ready. Defaults to waiting for all.

    Arguments:
        client {VNS3Client}

    Keyword Arguments:
        import_uuids {List[str]} - list of import uuids to filter on
        timeout {float}

    Raises:
        CohesiveSDKException

    Returns:
        Bool
    """
    start_time = time.time()
    resp_data = client.network_edge_plugins.get_container_system_images()
    images = resp_data.response.images
    if not images:
        if import_uuids is not None:
            raise CohesiveSDKException("No container images found.")
        return True

    if all([i.status == "Ready" for i in images]):
        return True

    time.sleep(interval)
    while time.time() - start_time < timeout:
        resp_data = client.network_edge_plugins.get_container_system_images()
        images = resp_data.response.images
        if all([i.status == "Ready" for i in images if i.import_id in import_uuids]):
            return True
        time.sleep(interval)

    raise CohesiveSDKException(
        "Timeout: Images failed to enter ready state [timeout=%s seconds, host=%s]"
        % (timeout, client.host_uri)
    )


def get_image_id_from_import(client, import_id):
    """Fetch Image ID given import uuid

    Arguments:
        client {VNS3Client}
        import_id {str}

    Returns:
        str - image ID
    """
    resp_data = client.network_edge_plugins.get_container_system_images(uuid=import_id)
    images = resp_data.response.images
    if not images:
        raise CohesiveSDKException("Couldnt find image for import id %s" % import_id)

    image = images[0]
    return image.id


def search_images(client, image_name):
    """Search plugin images by name

    Arguments:
        client {VNS3Client}
        image_name {str}

    Raises:
        CohesiveSDKException: [description]

    Returns:
        ContainerImage
    """
    resp_data = resp_data = client.network_edge_plugins.get_container_system_images()
    images = resp_data.response.images
    if images is None:
        raise CohesiveSDKException("Container system is not running")
    if len(images) == 0:
        return None

    for image in images:
        if image.image_name.lower() == image_name.lower():
            return image
    return None
