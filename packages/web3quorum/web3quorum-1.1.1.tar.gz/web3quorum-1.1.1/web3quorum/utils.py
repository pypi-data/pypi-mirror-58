from urllib.parse import urlparse


def enode_to_raft_id(w3, enode: str) -> int:
    """Resolves enode URI or Id into raft Id."""
    if enode.startswith('enode://'):
        enode = urlparse(enode).username
    cluster = w3.raft.cluster
    for node in cluster:
        if str(node.get('nodeId')) == enode:
            return int(node.get('raftId'))


def hostname_to_raft_id(w3, hostname: str) -> int:
    """Resolves hostname into raft Id."""
    cluster = w3.raft.cluster
    for node in cluster:
        if str(node.get('hostname')) == hostname:
            return int(node.get('raftId'))
