
def ip2ipam(a):
    """convert an IPv4 IP Address to phpIPAM decimal IP Address"""

    s_bin = ''

    try:

      if '.' in str(a):
      
        a = a.split('.')

        for octet in a:

          s_bin = s_bin + '{0:08b}'.format(int(octet))

    except Exception as e:

        raise AnsibleFilterError("to_nice_yaml - %s" % to_native(e), orig_exc=e)


    return int(s_bin, 2)


def ipam2ip(a):
    """convert a phpIPAM decimal IP Address to an IPv4 IP Address"""

    s_bin = ''

    try:

      s_bin = '{0:08b}'.format(int(a))

      s_bin = str(
        str(int(s_bin[0:8], 2)) + '.' + 
        str(int(s_bin[8:16], 2)) + '.' + 
        str(int(s_bin[16:24], 2)) + '.' + 
        str(int(s_bin[24:32], 2))
      )

    except Exception as e:

        raise AnsibleFilterError("to_nice_yaml - %s" % to_native(e), orig_exc=e)

    return s_bin


class FilterModule(object):
    """my format filters."""


    def filters(self):
        """Return the filter list."""
        return {
            'ip2ipam': ip2ipam,
            'ipam2ip': ipam2ip
        }
