# modbus with accept-gaps: parsing resumes after a TCP gap

Same capture as modbus-tcp-gap-default. With the proposed
app-layer.protocols.modbus.accept-gaps: yes, the parser drops the partial frame and
resynchronizes after the gap: only the request that was cut is lost (19 of 20 on
10.128.0.0), and the gap is not counted as an app-layer error.
