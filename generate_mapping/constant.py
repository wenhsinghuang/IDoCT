import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CUR_DIR, "../../")

CTEST_HADOOP_DIR = os.path.join(APP_DIR, "hadoop")
CTEST_HBASE_DIR = os.path.join(APP_DIR, "hbase")
CTEST_ZOOKEEPER_DIR = os.path.join(APP_DIR, "zookeeper")
CTEST_ALLUXIO_DIR = os.path.join(APP_DIR, "alluxio")
CTEST_CAMEL_DIR = os.path.join(APP_DIR, "camel")

MODULE_PATH = {
    "hadoop-common": CTEST_HADOOP_DIR,
    "hadoop-hdfs": CTEST_HADOOP_DIR,
    "hbase-server": CTEST_HBASE_DIR,
    "alluxio-core": CTEST_ALLUXIO_DIR,
    "camel-core": CTEST_CAMEL_DIR
}

SRC_SUBDIR = {
    "hadoop-common": "hadoop-common-project/hadoop-common",
    "hadoop-hdfs": "hadoop-hdfs-project/hadoop-hdfs",
    "hbase-server": "hbase-server",
    "zookeeper-server": "zookeeper-server",
    "alluxio-core": "core",
    "camel-core": "core"
}

MVN_TEST_PATH = {
    "hadoop-common": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"]),
    "hadoop-hdfs": os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"]),
    "hbase-server": os.path.join(CTEST_HBASE_DIR, SRC_SUBDIR["hbase-server"]),
    "zookeeper-server": os.path.join(CTEST_ZOOKEEPER_DIR, SRC_SUBDIR["zookeeper-server"]),
    "alluxio-core": os.path.join(CTEST_ALLUXIO_DIR, SRC_SUBDIR["alluxio-core"]),
    "camel-core": os.path.join(CTEST_ALLUXIO_DIR, SRC_SUBDIR["camel-core"]),
}

LOCAL_CONF_PATH = {
    "hadoop-common": "results/hadoop-common/conf_params.txt",
    "hadoop-hdfs": "results/hadoop-hdfs/conf_params.txt",
    "hbase-server": "results/hbase-server/conf_params.txt",
    "zookeeper-server": "results/zookeeper-server/conf_params.txt",
    "alluxio-core": "results/alluxio-core/conf_params.txt",
    "camel-core": "results/camel-core/conf_params.txt"
}

SUREFIRE_SUBDIR = "target/surefire-reports/*"

CTEST_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-common"], SUREFIRE_SUBDIR)
    ],
    "hadoop-hdfs": [
        os.path.join(CTEST_HADOOP_DIR, SRC_SUBDIR["hadoop-hdfs"], SUREFIRE_SUBDIR)
    ],
    "hbase-server": [
        os.path.join(CTEST_HBASE_DIR, "hbase-server", SUREFIRE_SUBDIR)
    ],
    "zookeeper-server": [
        os.path.join(CTEST_ZOOKEEPER_DIR, "zookeeper-server", SUREFIRE_SUBDIR)
    ],
    "alluxio-core": [
        os.path.join(CTEST_ALLUXIO_DIR, "core/base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/fs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/client/hdfs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/proxy", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/worker", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, "core/server/master", SUREFIRE_SUBDIR)
    ],
    "camel-core": [
        os.path.join(CTEST_CAMEL_DIR, "core/camel-util", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-api", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-catalog", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-support", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-management-api", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-management", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-base-engine", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-xml-io-util", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-xml-jaxp", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-cluster", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-engine", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-languages", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-model", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-processor", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-reifier", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-xml-io", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-xml-jaxb", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-xml", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-cloud", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-health", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-console", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-main", SUREFIRE_SUBDIR),
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core-all", SUREFIRE_SUBDIR)
    ]
}

LOCAL_SUREFIRE_SUFFIX = "surefire-reports/*"

LOCAL_SUREFIRE_PATH = {
    "hadoop-common": [
        os.path.join("surefire-reports/common/hadoop-common", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hadoop-hdfs": [
        os.path.join("surefire-reports/hdfs/hadoop-hdfs", LOCAL_SUREFIRE_SUFFIX)
    ],
    "hbase-server": [
        os.path.join("surefire-reports/hbase/hbase-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "zookeeper-server": [
        os.path.join("surefire-reports/zk/zookeeper-server", LOCAL_SUREFIRE_SUFFIX)
    ],
    "alluxio-core": [
        os.path.join("surefire-reports/alluxio-core", LOCAL_SUREFIRE_SUFFIX)
    ],
    "camel-core": [
        os.path.join("surefire-reports/camel-core", LOCAL_SUREFIRE_SUFFIX)
    ]
}
