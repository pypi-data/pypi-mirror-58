==================
MoiToi Docker Hive
==================


.. image:: https://img.shields.io/pypi/v/moitoi_docker_hive.svg
        :target: https://pypi.python.org/pypi/moitoi_docker_hive

.. image:: https://img.shields.io/travis/kepsic/moitoi_docker_hive.svg
        :target: https://travis-ci.org/kepsic/moitoi_docker_hive

.. image:: https://readthedocs.org/projects/moitoi-docker-hive/badge/?version=latest
        :target: https://moitoi-docker-hive.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




MoiToi Docker Hive is simple docker containers orchestrator, which
deploys services as containers and spreads the workloads between number of nodes
and acting as cluster.


* Free software: MIT license
* Documentation: https://moitoi-docker-hive.readthedocs.io.


Features
--------

Images
######


Following images is deployed on first cluster init

+------------+-----------------------------------+
| Image      | Description                       |
+============+===================================+
| mdh_lb     | NGINX load balancer image         |
+------------+-----------------------------------+
| mdh_backend| Backend image                     |
+------------+-----------------------------------+
| mdh_elsa   | REST API and load balancer        |
|            | config handler                    |
+------------+-----------------------------------+
| mdh_grafana| Grafana instance                  |
+------------+-----------------------------------+
| mdh_prom   | Prometheus instance               |
+------------+-----------------------------------+
| mdh_statsd | Proetheus stats exporter          |
+------------+-----------------------------------+


Every service instance have a Telegraf entrypoint scraped by Prometheus instance.
Prometheus data is visualized by Grafana instance


Endpoints
#########


/Service
    params
        * cluster_id - mdhxx.....
        * add_service - Initializes new cluster with one backned node and monitoring infra
        * add_node - add's node to cluster
        * rm_node - removes node from cluster


    * GET - Without params it will return all clusters and nodes
    * POST - Creates new cluster as specified in JSON input.
        .. code-block:: JSON

                { "clusters": "1",
                  "replicas" : "1" }
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


ToDo
--------
    * More documentation
    * Increase security level by adding authentitcation
    * Decrease docker socket access for ELSA. Currently its fully exposed for all services.
    * Remote provider for example VMWare, XEN, etc
    * Implement tests

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
