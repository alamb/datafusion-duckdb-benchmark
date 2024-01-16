# Runs several benchmark

# q33 can't complete in datafusion 25
# so need to comment itout
#DATAFUSION_CLI=./datafusion-cli-25.0.0 CREATE=create-single-datafusion.sql bash run-datafusion.sh

DATAFUSION_CLI=./datafusion-cli-34.0.0 CREATE=create-single-datafusion.sql bash run-datafusion.sh
