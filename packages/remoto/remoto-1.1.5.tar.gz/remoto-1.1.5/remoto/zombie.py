import remoto
import remoto.process
import time

count = 15
while count:
    conn1 = remoto.Connection('node1')
    conn2 = remoto.Connection('node1')
    out, err, code = remoto.process.check(
        conn2, ['true'])
    out, err, code = remoto.process.check(
        conn1, ['true'])
    print('[%s] out %s err %s code %s' % (count, out, err, code))
    conn1.exit()
    conn2.exit()
    #conn.gateway.close()
    #conn.gateway._io.kill()
    #conn.gateway._io.wait()
    count -= 1
    time.sleep(1)
