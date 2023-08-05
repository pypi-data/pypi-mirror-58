# Allenpoly

Extension of AllenNLP that allows to train models in Polyaxon cluster. 

Local usage:
```
$ export POLYAXON_NO_OP=true
$ allenpoly train config.json --include-package your_package --serialization_dir ./experiment_dir/  
```

Polyaxon cluster usage:

Example experiment file:
```
...

run:
  cmd: allenpoly train config.json --include-package your_package --serialization_dir $POLYAXON_RUN_OUTPUTS_PATH
```