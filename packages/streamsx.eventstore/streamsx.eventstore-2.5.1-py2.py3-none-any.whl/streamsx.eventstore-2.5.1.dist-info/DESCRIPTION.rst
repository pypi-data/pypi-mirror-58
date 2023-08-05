Overview
========

Provides a function to insert IBM Streams tuple data into a table in IBM Db2 Event Store.

IBM Db2 Event Store is an in-memory database designed to rapidly ingest and analyze streamed data in event-driven applications. It provides the fabric for fast data with its ability to process massive volume of events in real-time, coupled with optimization for streamed data performance for advanced analytics and actionable insights.

This package exposes the `com.ibm.streamsx.eventstore` toolkit and `com.ibm.streamsx.jdbc` toolkit as Python methods.

Supported versions:

* Db2 Event Store 1.x: streamsx.eventstore version 1.x
* Db2 Event Store 2.x: streamsx.eventstore version 2.x

Sample
======

A simple example of a Streams application inserting rows to
a table in a Db2 Event Store database::

    from streamsx.topology.topology import Topology
    from streamsx.topology.schema import CommonSchema, StreamSchema
    from streamsx.topology.context import submit
    from streamsx.topology.context import ContextTypes
    import streamsx.spl.toolkit
    import streamsx.eventstore as es

    topo = Topology('EventStoreSample')

    # provide connection endpoint information
    es_connection = 'HostIP:Port1;HostIP:Port2'

    # generate sample tuples with the schema of the target table
    s = topo.source([1,2,3,4,5,6,7,8,9])
    schema=StreamSchema('tuple<int32 id, rstring name>').as_tuple()
    s = s.map(lambda x : (x,'X'+str(x*2)), schema=schema)

    # insert tuple data into table as rows
    res = es.insert(s, connection=es_connection, database='TESTDB', table='SampleTable', primary_key='id', partitioning_key='id')

    submit (ContextTypes.DISTRIBUTED, topo)
    # The Streams job is kept running.


Documentation
=============

* `streamsx.eventstore package documentation <http://streamsxeventstore.readthedocs.io>`_


