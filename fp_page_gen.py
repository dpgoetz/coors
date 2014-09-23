#!/usr/bin/python
import sys
from time import time
import hmac
from hashlib import sha1

html = '''
<html>
<b>Does CF FormPost Work?</b><br>

    <form action="%(endpoint)s" method="POST"
          enctype="multipart/form-data">
      <input type="hidden" name="redirect" value="%(redirect)s" />
      <input type="hidden" name="max_file_size" value="104857600" />
      <input type="hidden" name="max_file_count" value="10" />
      <input type="hidden" name="expires" value="%(expires)d" />
      <input type="hidden" name="signature" value="%(sig)s" />
      <input type="file" name="file1" /><br />
      <input type="submit" />
    </form>

</html>
'''

def main():
    if len(sys.argv) != 5:
        print
        print 'Invalid args:'
        print './fp_page_gen.py https://storage101.ord1.clouddrive.com/v1/MossoCloudFS_12345/container/prefix http://the-redirect.com tempurl-key ttl'
        print
        sys.exit(1)

    endpoint, redirect, key, ttl = sys.argv[1:]
    max_size = 104857600
    max_count = 10

    junk, path = endpoint.split('clouddrive.com')

    expires = int(time() + int(ttl))
    hmac_body = '%s\n%s\n%s\n%s\n%s' % (
        path, redirect, max_size, max_count, expires)

    sig = hmac.new(key, hmac_body, sha1).hexdigest()

    print html % {'endpoint': endpoint, 'redirect': redirect,
                  'expires': expires, 'sig': sig}

if __name__ == '__main__':
    main()
