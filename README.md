fp_page_gen.py

you can run that like this:

./fp_page_gen.py https://storage101.ord1.clouddrive.com/v1/MossoCloudFS_12345/container/prefix http://the-redirect.com tempurl-key ttl > test.html

ttl would just be an integer like 900

and then 
python -m SimpleHTTPServer

and then in a browser go to 127.0.0.1:8000/test.html and upload a file.

The other one is a lot cooler. Its a flask app one of our guys put together to try stuff out:

app.py

with templates/dropzone.html

If you have flask installed: ( http://flask.pocoo.org )

then you can run 

python app.py https://storage101.ord1.clouddrive.com/v1/MossoCloudFS_12345/container/prefix tempurl-key

with your storage url and tempurl key. Go to:

http://127.0.0.1:5000/dropzone

and magically upload files into your CF container. (As long as you have x-container-meta-access-control-allow-origin:* set on the container you are pointing at).

Hopefully this will help clear things up.

PS (if you want formpost to work over ajax leave your redirect = ''.)
