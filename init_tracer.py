from jaeger_client import Config, ConstSampler
from jaeger_client.reporter import InMemoryReporter

from flask_opentracing import FlaskTracing

def init():
    config = Config(
        service_name='test',
        config={
            'trace_id_header': 'Trace_ID',
            'baggage_header_prefix': 'Trace-Attr-',
        })
    reporter = InMemoryReporter()
    tracer = config.create_tracer(
        reporter=reporter,
        sampler=ConstSampler(True),
    )
    tracing = FlaskTracing(tracer, True, app)
