from collections import namedtuple

Link = namedtuple("Link", "source, target, weight")
Tree = namedtuple("Tree", "path, flow, state_id, physical_id")


def read_links(filename, weight_type=float):
    links = []

    with open(filename, "r") as f:
        context = None

        for line in f:
            if line.startswith("#"):
                continue

            l = line.lower()

            if l.startswith("*links"):
                context = "*links"
                continue
            elif l.startswith("*"):
                context = None
                continue

            if context == "*links":
                source, target, weight = line.split()
                links.append(Link(int(source), int(target), weight_type(weight)))

    return links


def read_tree(filename, states=True):
    tree = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith("#"):
                continue

            if states:
                path, flow, *_, state_id, physical_id = line.split()
                state_id = int(state_id)
            else:
                path, flow, *_, physical_id = line.split()
                state_id = None

            path = tuple(map(int, path.split(":")))
            tree.append(Tree(path, float(flow), state_id, int(physical_id)))

    return tree


if __name__ == "__main__":
    net = read_links("test/training_seed0_order2_0.net")
    print(net[0])
    print(net[1])
    tree = read_tree("test/training_seed0_order2_0_states.tree")
    print(tree)
