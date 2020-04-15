import com.py.train.Oops.Polygon as poly


### sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_file1_method1():
    x=5
    y=6
    assert x+1 == y,"test failed"
    assert x != y,"test failed"

def test_square():
    sq=poly.Square(10)

    sq.calculateParameter()
    sq.calculateArea()
    assert sq.area==100
    assert sq.para==40