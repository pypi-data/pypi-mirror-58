# dynamite

Use dynamite to keep a postgres replica of one or more dynamodb
table. At its core, dynamite is an AWS Lambda event handler for
processing dynamodb streams record events and shuttling those record
events into an associated postgres database.
