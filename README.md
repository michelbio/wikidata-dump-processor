# wikidata-dump-processor
import Wikidata json dump (.json.bz2) into Mongodb

- Index fields: `id`, `sitelinks.enwiki.title`

- [Partial Index](https://docs.mongodb.com/manual/core/index-partial/) for [Covered Query](https://docs.mongodb.com/manual/core/query-optimization/#covered-query): `{ sitelinks.enwiki.title: 1, id: 1 }`

- [Partial Index](https://docs.mongodb.com/manual/core/index-partial/) for [Covered Query](https://docs.mongodb.com/manual/core/query-optimization/#covered-query): `{ labels.en.value: 1, id: 1 }`

- Performance: ~3 hours for importing, ~1 hour for indexing (`--nworker 12`, `--chunk_size 10000`)