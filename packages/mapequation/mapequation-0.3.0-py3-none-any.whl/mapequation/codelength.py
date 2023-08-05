import numpy as np


def codelength(links, tree, entropy_function=np.log, state_network=True, directed=False):
    if directed:
        source, target, weight = zip(*links)
    else:
        source, target, weight = [], [], []
        for s, t, w in links:
            source.append(s)
            source.append(t)
            target.append(t)
            target.append(s)
            weight.extend((w, w))

    if state_network:
        modules, _, state_ids, physical_ids = zip(*tree)
    else:
        modules, _, state_ids, physical_ids = zip(*((path, flow, phys_id, phys_id)
                                                    for path, flow, _, phys_id in tree))

    level = [len(path) - 2 for path in modules]  # top level is level 0
    level = np.array(level)

    physical_ids = np.array(physical_ids)

    module_per_level = {":".join(str(l) for l in path[:(j + 1)])
                        for path in modules
                        for j in range(len(path) - 1)}

    module_index = {module: i for i, module in enumerate(module_per_level)}

    # convert state node labels to integers from range(0, num_states)
    node_id = {int(n): i for i, n in enumerate(state_ids)}

    source_id, target_id = list(zip(*((node_id[n1], node_id[n2])
                                      for n1, n2 in zip(source, target))))

    # convert module label to integer (for each level)
    num_states = len(state_ids)
    num_levels = np.max(level) + 1
    module_per_level = -1 * np.ones(num_states * num_levels).reshape(num_states, num_levels).astype(int)
    for i, path in enumerate(modules):
        for j in range(len(path) - 1):
            mod_per_level = ":".join(str(l) for l in path[:(j + 1)])
            module_per_level[i][j] = module_index[mod_per_level]

    module_id_per_level = -1 * np.ones(num_states * num_levels).reshape(num_states, num_levels).astype(int)
    for j in range(num_levels):
        module_per_level_j = module_per_level[:, j]
        modules = np.unique(module_per_level_j[module_per_level_j > -1])
        D = {module: i for i, module in enumerate(modules)}
        for i in range(num_states):
            if module_per_level_j[i] > -1:
                module_id_per_level[i][j] = D[module_per_level_j[i]]

    k_in = np.zeros(num_states)  # node degree
    for alpha, w in zip(target_id, weight):
        k_in[alpha] += w
    norm_M = 1.0 / np.float(np.sum(k_in))

    enter, exit_ = {}, {}
    for l in range(num_levels):
        module_id = module_id_per_level[:, l]
        modules = np.unique(module_id[module_id > -1])  # list of unique module ids
        num_modules = len(modules)
        enter[l], exit_[l] = np.zeros(num_modules), np.zeros(num_modules)  # number of links to/from module
        for alpha, beta, w in zip(source_id, target_id, weight):
            i = module_id[alpha]
            j = module_id[beta]
            if i != j:
                if i > -1:
                    exit_[l][i] += w
                if j > -1:
                    enter[l][j] += w

    L_M = 0.0  # average codelength

    # ---------------------------- the finest level ----------------------------
    out_modules = []
    for l in range(num_levels):
        module_id = module_id_per_level[:, l]
        modules = np.unique(module_id[level == l])
        num_modules = len(modules)
        n_i_exit = exit_[l]

        # H_Pi: the average length of codewords in module codebook i
        H_Pi, p_i = np.zeros(num_modules), np.zeros(num_modules)
        for i, mod_id in enumerate(modules):
            k_in_m = k_in[module_id == mod_id]
            physical_id = physical_ids[module_id == mod_id]
            n_i = [n_i_exit[mod_id]]
            for unique_phys_id in np.unique(physical_id):
                n_i.append(np.sum(k_in_m[physical_id == unique_phys_id]))
            n_i = np.array(n_i)
            p_i[i] = np.sum(n_i) * norm_M
            n_i = n_i[n_i > 0]
            if len(n_i) > 0:
                H_Pi[i] = (np.log(np.sum(n_i)) - (1.0 / np.sum(n_i)) * np.sum(n_i * entropy_function(n_i))) / np.log(2)

        L_m = np.sum(p_i * H_Pi)  # module codebook
        L_M += L_m
        out_modules.append(L_m)

    # ---------------------------- intermediate level ----------------------------
    out_index = []
    for l in range(1, num_levels):
        module_mn_id = module_id_per_level[:, l]
        module_mn_id = module_mn_id[level >= l]
        module_m_id = module_id_per_level[:, l - 1]
        module_m_id = module_m_id[level >= l]
        modules = np.unique(module_m_id)
        num_modules = len(modules)
        n_m_exit = exit_[l - 1]
        n_mn_enter = enter[l]

        # H_Qm: the average length of codewords in submodule m
        H_Qm = np.zeros(num_modules)
        q_m_total = np.zeros(num_modules)
        for i in range(num_modules):
            n_i = np.insert(n_mn_enter[np.unique(module_mn_id[module_m_id == modules[i]])], 0, n_m_exit[modules[i]])
            n_i = n_i[n_i > 0]
            if len(n_i) > 0:
                H_Qm[i] = (np.log(np.sum(n_i)) - (1.0 / np.sum(n_i)) * np.sum(
                    n_i * entropy_function(n_i))) / np.log(2)
                q_m_total[i] = np.sum(n_i) * norm_M

        L_i = np.sum(q_m_total * H_Qm)  # index codebook
        L_M += L_i
        out_index.append(L_i)

    # ---------------------------- the coarsest level ----------------------------
    n_m_enter = enter[0]
    module_per_level_j = n_m_enter[n_m_enter > 0]

    if len(module_per_level_j) > 1:
        H_Q = (np.log(np.sum(module_per_level_j)) - (1.0 / np.sum(module_per_level_j)) * np.sum(
            module_per_level_j * entropy_function(module_per_level_j))) / np.log(2)
    else:
        H_Q = 0.0

    q_m_enter = n_m_enter * norm_M
    L_i = np.sum(q_m_enter) * H_Q
    L_M += L_i

    return L_M


if __name__ == "__main__":
    from grassberger import entropy_function, coefficients
    from read_file import read_links, read_tree

    train_links = read_links("test/training_seed0_order2_1.net", weight_type=int)
    validation_links = read_links("test/validation_seed0_order2_1.net", weight_type=int)
    tree = read_tree("test/training_seed0_order2_1_states.tree")

    Lm = codelength(train_links, tree)
    print(f"Naive: training {Lm} bits")

    Lm = codelength(validation_links, tree)
    print(f"Naive: validation: {Lm} bits")

    Gn = coefficients(1000000)

    Lm = codelength(train_links, tree, entropy_function(Gn))
    print(f"Grassberger: training {Lm} bits")

    Lm = codelength(validation_links, tree, entropy_function(Gn))
    print(f"Grassberger: validation {Lm} bits")
