from graphs import Digraph 

def test():
    digraph = Digraph()

    assert len(digraph) == 0

    for i in range(10):
        assert len(digraph) == i
        digraph.add_node(i)
        assert len(digraph) == i + 1

    digraph.remove_node(8)
    assert len(digraph) == 9
    digraph.remove_node(9)
    assert len(digraph) == 8
    assert digraph.number_of_edges() == 0

    digraph.add_edge(8, 7, 20.0)
    assert digraph.has_edge(8, 7)
    assert 20.0 == digraph.get_edge_weight(8, 7)
    assert digraph.number_of_edges() == 1

    assert 20.0 == digraph.get_edge_weight(8, 7)
    assert digraph.number_of_edges() == 1

    digraph.add_edge(9, 8, 10.0)
    assert digraph.number_of_edges() == 2
    assert digraph.get_edge_weight(9, 8) == 10.0
    assert digraph.has_edge(9, 8)
    assert not digraph.has_edge(8, 9)
    digraph.remove_node(8)
    assert not digraph.has_edge(9, 8)
    assert digraph.number_of_edges() == 0

    digraph.remove_node(5)
    assert len(digraph) == 8

    digraph.add_edge(0, 3, 1.0)
    digraph.add_edge(1, 3, 2.0)
    digraph.add_edge(3, 6, 3.0)
    digraph.add_edge(3, 7, 4.0)

    assert digraph.number_of_edges() == 4

    assert 0 in digraph.get_parents_of(3)
    assert 1 in digraph.get_parents_of(3)
    assert 6 in digraph.get_children_of(3)
    assert 7 in digraph.get_children_of(3)

    try:
        digraph.get_edge_weight(3, 100)
        assert False
    except Exception:
        pass

    try:
        digraph.get_edge_weight(100, 3)
        assert False
    except Exception:
        pass

    try:
        digraph.get_edge_weight(2, 3)
        assert False
    except Exception:
        pass

test()