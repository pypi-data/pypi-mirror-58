# boiler

## installation

```bash
# for yaml.CLoader support
apt install libyaml-dev

# install boiler tools
pip3 install -e .

# set token for stumpf and boto3.
# these are only necessary to communicate with stumpf server
# and AWS.  Not needed for local operations
export X_STUMPF_TOKEN=""
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""

boiler --help
```

See [boto3 docs](https://pypi.org/project/boto3/) for additional info about AWS config.

## usage

### kpf

KPF data validation

```bash
# locally validate KPF yaml
boiler kpf validate \
  --geom examples/kpf/geom.yml \
  --activities examples/kpf/activities.yml \
  --types examples/kpf/types.yml | jq
```

Example kpf can be found in `examples/kpf/`

### video ingest

Video ingestion can be done one-off or through a batch CSV file.

```bash
# one-off
boiler video ingest --help

# bulk using a manifest csv file
boiler video bulk-ingest --help
```

Notes on ingest behavior:

* Not all fields are requred.
* If `gtag`, `location`, etc. are parseable from the video name, they will be.
* You can override any parsed or guessed fields by setting them explicitly.
* One of `local_path` or `s3_path` is required.
  * If `local_path` is set, boiler will upload the video to s3 and attempt transcoding.
  * If `s3_path` is set, boiler will assume transcoding is complete and expect `frame_rate`, `duration`, etc. to be set.

Example bulk ingest files can be found in `examples/`

## design

design for cli commands follows some simple guidelines:

* commands produce a single JSON document (map or array) as output on stdout in all conditions.
* input data and REST errors cause boiler to exit with status code 1.  error information is JSON on stdout.
* exceptions not related to input data or REST operations should not be caught or handled; They are bugs.
* additional logging and metrics, especially for batch operations, may be printed to stderr.
* any output on stderr has no guaranteed format, though in most cases it should be human-readable lines of text.
* click.argument should not be used.  prefer click.option

TL;DR you can confidently pipe any boiler command to `jq`
