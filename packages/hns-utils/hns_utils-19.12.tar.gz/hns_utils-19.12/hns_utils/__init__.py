# Just some common helpful functions like OS agnostic ping
import subprocess
from platform import system


def ping(host='127.0.0.1'):
    """
    A simple ping to check reachability to the host. Its OS agnostic. It uses the OS 'ping' command
    :param host: host ip or name. Must be IPv4
    :type host: str
    :return: dict with :key: host_status, pkt_lost, rtt_average and delta_rtt
    """

    ping_result = {}
    if system().lower() == 'windows':
        ping_cmd = 'ping -n 5 -w 2000 {0}'.format(host)
        try:
            print('\r\nChecking reachability to {0}\r\n'.format(host))
            response_decoded = subprocess.check_output(ping_cmd, shell=True).decode()
            if 'TTL' in response_decoded:
                tmp_pkt_lost = response_decoded[
                               response_decoded.rfind('Lost'):
                               response_decoded.find(',', response_decoded.rfind('Lost'))
                               ]
                tmp_rtt_avg = response_decoded[
                              response_decoded.rfind('Average'):
                              response_decoded.rfind('\r')
                              ]
                tmp_rtt_min = response_decoded[
                              response_decoded.rfind('Minimum'):
                              response_decoded.find(',', response_decoded.rfind('Minimum'))
                              ]
                tmp_rtt_max = response_decoded[
                              response_decoded.rfind('Maximum'):
                              response_decoded.find(',', response_decoded.rfind('Maximum'))
                              ]
                pkt_lost = int(tmp_pkt_lost[tmp_pkt_lost.find('=') + 2])
                rtt_avg = int(tmp_rtt_avg[tmp_rtt_avg.find('=') + 2:tmp_rtt_avg.rfind('ms')])
                rtt_min = int(tmp_rtt_min[tmp_rtt_min.find('=') + 2:tmp_rtt_min.rfind('ms')])
                rtt_max = int(tmp_rtt_max[tmp_rtt_max.find('=') + 2:tmp_rtt_max.rfind('ms')])
                delta_rtt = abs(rtt_max - rtt_min)
                ping_result['host_status'] = 'Online'
                ping_result['pkt_lost'] = pkt_lost
                ping_result['rtt_average'] = rtt_avg
                ping_result['delta_rtt'] = delta_rtt
            else:
                ping_result['host_status'] = 'Offline'
                ping_result['pkt_lost'] = ''
                ping_result['rtt_average'] = ''
                ping_result['delta_rtt'] = ''
        except:
            ping_result['host_status'] = 'Offline'
            ping_result['pkt_lost'] = ''
            ping_result['rtt_average'] = ''
            ping_result['delta_rtt'] = ''
        return ping_result

    else:  # if system is linux
        ping_cmd = 'ping -c 5 {0}'.format(host)
        try:
            print('\r\nChecking reachability to {0}\r\n'.format(host))
            response_decoded = subprocess.check_output(ping_cmd, shell=True).decode()
            if 'ttl' in response_decoded:
                tmp_pkt_lost = response_decoded[
                               response_decoded.rfind('received'):
                               response_decoded.rfind('packet loss')
                               ]
                tmp_rtt_values = response_decoded[
                                 response_decoded.rfind('=') + 2:
                                 response_decoded.rfind('ms') - 1
                                 ]
                rtt_values = tmp_rtt_values.split('/')
                pkt_lost = int(tmp_pkt_lost[tmp_pkt_lost.find(',') + 2:tmp_pkt_lost.rfind('%')])
                rtt_avg = int(round(float(rtt_values[1])))
                delta_rtt = abs(int(round(float(rtt_values[-1]))))
                packet_lost_values = {0: 0, 20: 1, 40: 2, 60: 3, 80: 4, 100: 5}
                ping_result['host_status'] = 'Online'
                ping_result['pkt_lost'] = packet_lost_values[pkt_lost]
                ping_result['rtt_average'] = rtt_avg
                ping_result['delta_rtt'] = delta_rtt
            else:
                ping_result['host_status'] = 'Offline'
                ping_result['pkt_lost'] = ''
                ping_result['rtt_average'] = ''
                ping_result['delta_rtt'] = ''
        except:
            ping_result['host_status'] = 'Offline'
            ping_result['pkt_lost'] = ''
            ping_result['rtt_average'] = ''
            ping_result['delta_rtt'] = ''
        return ping_result
