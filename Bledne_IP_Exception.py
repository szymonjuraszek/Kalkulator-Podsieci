class Bledne_IP_Exception(Exception):
   def __int__(self,ip):
       super.__init__("Podano niepoprawne IP!".format(ip))


