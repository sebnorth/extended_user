import unittest
from milo import Milo

class TestClass(unittest.TestCase):
    def setUp(self):
        data='1/2/3'
        self.milo = Milo(data=data)
        #self.milo.printdates()
        # print('self.milo.milo_earliest_possible ' + str(self.milo.milo_earliest_possible()))
    def test_initialized(self):
        assert type(self.milo.data) == str
        assert type(self.milo.milolist) == list
        self.assertEqual(self.milo.x, 1)
        self.assertEqual(self.milo.y, 2)
        self.assertEqual(self.milo.z, 3)
        self.assertEqual(self.milo.milolist[0], (1,2,3))
        self.assertEqual(self.milo.milolist, [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1) ])
        #self.assertEqual(self.milo.milo_date_possible(str(self.milo.milolist[0])),'2001-02-03')
    def test_milo_date_possible(self):
        data='1/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2001-02-03')
        data='10/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2010-02-03')
        data='100/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2100-02-03')
        data='2000/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2000-02-03')
        data='00/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2000-02-03')
        data='0/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2000-02-03')
        data='2014/02/3'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2014-02-03')
        data='2014/02/03'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2014-02-03')
        data='2014/2/03'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])),'2014-02-03')
        data='0/01/01'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), '2000-01-01')
        data='0/0/01'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='0/01/0'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='0/13/01'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='0/1/32'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='0/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), '2000-02-29')
        data='1/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='2100/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='100/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), 'False')
        data='4/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), '2004-02-29')
        data='2/1/1'
        self.milo = Milo(data=data)
        self.assertEqual(str(self.milo.milo_date_possible(self.milo.milolist[0])), '2002-01-01')
    
    def test_milo_answer(self):
        data='1/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-03')
        data='1/3/2'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-03')
        data='3/2/1'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-03')
        data='3/20/1'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-03-20')
        data='4/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2002-04-29')
        data='1/2/3'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-03')
        data='2100/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'is illegal')
        data='12/2/29'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2002-12-29')
        data='02/12/1'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-12')
        data='01/02/03'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-02-03')
        data='101/102/103'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'is illegal')
        data='0/0/2222'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'is illegal')
        data='31/12/2999'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2999-12-31')
        data='1/1/1'
        self.milo = Milo(data=data)
        self.assertEqual(self.milo.milo_answer(),'2001-01-01')



if __name__ == '__main__':
    unittest.main(exit=False)
