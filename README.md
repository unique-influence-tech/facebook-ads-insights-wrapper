## Introduction                                                                                                                                                                                                
A small tool to make bulk ads insights queries.

## Installation

Coming soon

## Usage

**Large Queries** :ballot_box_with_check: 

```python
>>> import package
>>> obj = package.insights.Controller(acct=xxxxxxxxxxxxx, prepared={})
>>> obj.schedule_job()
True
>>> obj.poll
'<[Job Id xxxxxxxxxxx 20% complete]>'
>>> obj.poll
'<[Job Id xxxxxxxxxxx 100% complete]>'
>>> obj.get
>>> obj.data
[{}, ... ,{}]
```

**Small Queries** :ballot_box_with_check: 

```python
>>> import package
>>> obj = package.insights.Controller(acct=xxxxxxxxxxxxx, prepared={})
>>> obj(prepared={})
>>> obj.data
```

## Testing

There's some testing coverage:

```bash
$ python -m package.tests.run

```
 
## Additional Notes

Coming soon

