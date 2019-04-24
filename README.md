# contrail-multi-cloud-creator
create multi cloud API objects

### Usage

```
contrail-multi-cloud-creator git:(master) python src/generate_mc_api_objects.py --help
usage: generate_mc_api_objects.py [-h] [--input INPUT]

Generate contrail go API schema objects needed to deploy CEM

optional arguments:
  -h, --help     show this help message and exit
  --input INPUT  path to the input file where config is stored
```

##### Example

Step1:
```
git clone https://github.com/madhukar32/contrail-multi-cloud-creator.git
```

Step2: Edit src/input_config.yaml

Step3: Run below commands
```
cd src
generate_mc_api_objects.py --input input_config.yaml
```
