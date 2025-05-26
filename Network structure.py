def get_link_name(nw_topology,arc):
  return str(nw_topology.cellSet[arc[0]]['name'])+'_'+str(nw_topology.cellSet[arc[-1]]['name'])

def get_node_name(nw_topology,node):
  return str(nw_topology.cellSet[node]['name'])

def init_Es(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'S'])

def init_Er(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[0]]['type'] == 'R'])

def init_Ec(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'C'])

def init_Ec_C1(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'C1'])

def init_Ec_C2(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'C2'])

def init_Ec_C3(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'C3'])

def init_Ec_C4(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['type'] == 'C4'])

def init_Ec_1(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['charging'] == 1])


def init_Ec_2(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['charging'] == 2])


def init_Ec_3(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['charging'] == 3])


def init_Ec_4(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys() if nw_topology.cellSet[k[-1]]['charging'] == 4])

def init_Ep(nw_topology):
  ret = []
  for k in nw_topology.arcSet.keys():
    tmp =[h for h in nw_topology.arcSet.keys() if h[0] == k[-1]]
    if len(tmp) != 0:
      for link in tmp:
        ret.append((get_link_name(nw_topology,k),get_link_name(nw_topology,link)))
  return sorted(ret)

def init_Ea(nw_topology):
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys()])

def init_Eo(nw_topology):
  Er = init_Er(nw_topology)
  Es = init_Es(nw_topology)
  return sorted([get_link_name(nw_topology,k) for k in nw_topology.arcSet.keys()
                 if get_link_name(nw_topology,k) not in Er and get_link_name(nw_topology,k) not in Es])

def init_T(nw_topology):
  return [i for i in range(0,nw_topology.ttm_params['maxT']+1)]

def init_K(nw_topology):
  ret ={}
  Er=init_Er(nw_topology)
  Es = init_Es(nw_topology)
  for k in nw_topology.arcSet.keys():
    if get_link_name(nw_topology,k) not in Er and get_link_name(nw_topology,k) not in Es:
      ret[get_link_name(nw_topology,k)] = nw_topology.arcSet[k]['max_density']
    else:
      ret[get_link_name(nw_topology,k)] = 9999
  return ret

def init_L(nw_topology):
  ret = {}
  for k in nw_topology.arcSet.keys():
    ret[get_link_name(nw_topology,k)] = nw_topology.arcSet[k]['len']
  return ret

def init_LinksIn(nw_topology):
  ret ={}
  Ea = init_Ea(nw_topology)
  for link in Ea:
    tmp = []
    for _link in Ea:
      if _link.split('_')[-1] == link.split('_')[0]:
        tmp.append(_link)
    ret[link] = list(set(tmp))
  return ret

def init_LinksOut(nw_topology):
  ret ={}
  Ea = init_Ea(nw_topology)
  for link in Ea:
    tmp = []
    for _link in Ea:
      if _link.split('_')[0] == link.split('_')[-1]:
        tmp.append(_link)
    ret[link] = tmp
  return ret