#!/usr/bin/python

class Solution(object):
    def generate_permutations(self):
        ret = {}
        for i in xrange(1, 4):
            for j in xrange(1, 4):
                for k in xrange(1, 4):
                    for l in xrange(1, 4):
                        total = i+j+k+l
                        if total not in ret:
                            ret[total] = []

                        ret[total].append( (i, j, k, l) )
        return ret

    def valid_ip(self, ip):
        parts = ip.split('.')
        for part in parts:
            if len(part) > 1 and part[0] == '0':
                return False

            if int(part) == 0 and len(part) > 1:
                return False

            if int(part) > 255:
                return False

        return True

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        sl_original = list(s)
        perms = self.generate_permutations()

        if len(s) not in perms:
            return []

        possibilities = perms[len(s)]

        ret = []
        for i, j, k, l in possibilities:
            cumsum = 0
            sl = sl_original[:]

            cumsum += i
            sl.insert(cumsum, '.')
            cumsum += j + 1
            sl.insert(cumsum, '.')
            cumsum += k + 1
            sl.insert(cumsum, '.')
            ip = "".join(sl)
            if(self.valid_ip(ip)):
                ret.append(ip)

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses(""))
    print(s.restoreIpAddresses("25525511135"))
