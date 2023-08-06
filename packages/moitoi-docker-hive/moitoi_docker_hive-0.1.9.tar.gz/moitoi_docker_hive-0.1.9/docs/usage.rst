=====
Usage
=====

To use MoiToi Docker Hive in a python project::

    import moitoi_docker_hive
    handler = ClusterHandler()
    handler.setup_cluster_infra()

From CLI::

    #mdh init

    #mdh show

    #mdh show --cluster-id

    #mdh + --cluster-id mdhxxxx

    #mdh - --cluster-id mdhxxx

    #mdh delete --cluster-id mdhxx.....

After cluster setup u can navigate to http://localhost:5000 where you can add Service, Add/Remove Node, Show Service state
view Grafana graphs


With REST API:

/Service
    params
        * cluster_id - mdhxx.....
        * add_service - Initializes new cluster with one backned node and monitoring infra
        * add_node - add's node to cluster
        * rm_node - removes node from cluster


    * GET - Without params it will return all clusters and nodes
    * POST - Creates new cluster as specified in JSON input.
        .. code-block:: JSON

                { "clusters": "1", "replicas" : "1" }
    * PUT/PATCH - Updates cluster as specified in JSON input with with cluster_id param.
        .. code-block:: JSON

                { "replicas" : "2" }
    * DELETE - Delete cluster cluster cluster_id is specified

/State
    params
        * cluster_id - mdhxx.....


    * GET - Without params it will return all clusters and node states. With cluser_id returns cluster state

/Grafana
    Grafana interface. Default admin password is specified is first 10 characters of cluster_id

