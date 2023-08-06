"""Export a STEP file
"""

from onshape_client.client import Client
from onshape_client.configuration import Configuration
from onshape_client.onshape_url import OnshapeElement
from onshape_client.models.bt_translate_format_params import BTTranslateFormatParams
import time
import json
import os.path

client = Client()

# We're saving these files to the home directory ("~")
client.configuration.temp_folder_path = os.path.expanduser("~")


# Turn the URL into an "OnshapeElement"
url = "https://cad.onshape.com/documents/6294e51a225d251659adda53/w/7e81c11d14f7c7dbe1cc6f1f/e/f1c0095cc29ddff084e28cfb"
cube = OnshapeElement(url, client=client)

# Create the params. Note there are far more params that can be specified.
params = BTTranslateFormatParams(element_id=cube.eid, format_name="PDF", store_in_document=False)

# Call the client
response = client.drawings_api.translate_format4(cube.did, cube.wvm, cube.wvmid, cube.eid, bt_translate_format_params=params)

translation_id = response.id
state = response.request_state

# Long poll every 2 seconds until the translation is marked as done - alternatively you could submit a webhook
parsed_response = None
while state == 'ACTIVE':
    time.sleep(2)
    response = client.translation_api.get_translation(translation_id, _preload_content=False)
    parsed_response = json.loads(response.data.decode("UTF-8"))
    state = parsed_response["requestState"]

# Make the actual download when the translation is done, otherwise report the error
if state == "DONE":
    client.documents_api.download_external_data(cube.did, parsed_response["resultExternalDataIds"][0])
    print("File saved to " + client.configuration.temp_folder_path)
    print("Your access tokebn: " + client.oauth.access_token)
else:
    print("An error ocurred on the server! Here is the response: \n" + parsed_response)
"""
File saved to <temp_folder_path>
"""