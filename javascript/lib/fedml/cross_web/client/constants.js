export var constant;
(function (constant) {
  // FedML TRAINING PLATFORM
  constant.FEDML_TRAINING_PLATFORM_SIMULATION = 'simulation'
  constant.FEDML_TRAINING_PLATFORM_CROSS_SILO = 'cross_silo'
  constant.FEDML_TRAINING_PLATFORM_CROSS_DEVICE = 'cross_device'
  constant.FEDML_TRAINING_PLATFORM_DISTRIBUTED = 'distributed'
  // FedML TRAINING PLATFORM TYPE
  constant[constant.FEDML_TRAINING_PLATFORM_CROSS_SILO_TYPE = 1] = 'FEDML_TRAINING_PLATFORM_CROSS_SILO_TYPE'
  constant[constant.FEDML_TRAINING_PLATFORM_SIMULATION_TYPE = 2] = 'FEDML_TRAINING_PLATFORM_SIMULATION_TYPE'
  constant[constant.FEDML_TRAINING_PLATFORM_DISTRIBUTED_TYPE = 3] = 'FEDML_TRAINING_PLATFORM_DISTRIBUTED_TYPE'
  constant[constant.FEDML_TRAINING_PLATFORM_CROSS_DEVICE_TYPE = 4] = 'FEDML_TRAINING_PLATFORM_CROSS_DEVICE_TYPE'
  // FedML CROSS-SILO SCENARIO
  constant.FEDML_CROSS_SILO_SCENARIO_HORIZONTAL = 'horizontal'
  constant.FEDML_CROSS_SILO_SCENARIO_HIERARCHICAL = 'hierarchical'
  // FedML SIMULATION TYPE
  constant.FEDML_SIMULATION_TYPE_SP = 'sp'
  constant.FEDML_SIMULATION_TYPE_MPI = 'MPI'
  constant.FEDML_SIMULATION_TYPE_NCCL = 'NCCL'
  // FedML data
  constant.FEDML_DATA_CACHE_FOLDER = 'fedml_data'
  constant.FEDML_DATA_MNIST_URL = 'https://fedcv.s3.us-west-1.amazonaws.com/MNIST.zip'
  // FedML Algorithm
  constant.FedML_FEDERATED_OPTIMIZER_BASE_FRAMEWORK = 'base_framework'
  constant.FedML_FEDERATED_OPTIMIZER_FEDAVG = 'FedAvg'
  constant.FedML_FEDERATED_OPTIMIZER_FEDOPT = 'FedOpt'
  constant.FedML_FEDERATED_OPTIMIZER_FEDPROX = 'FedProx'
  constant.FedML_FEDERATED_OPTIMIZER_CLASSICAL_VFL = 'classical_vertical'
  constant.FedML_FEDERATED_OPTIMIZER_SPLIT_NN = 'split_nn'
  constant.FedML_FEDERATED_OPTIMIZER_DECENTRALIZED_FL = 'decentralized_fl'
  constant.FedML_FEDERATED_OPTIMIZER_FEDGAN = 'FedGAN'
  constant.FedML_FEDERATED_OPTIMIZER_FEDAVG_ROBUST = 'FedAvg_robust'
  constant.FedML_FEDERATED_OPTIMIZER_FEDAVG_SEQ = 'FedAvg_seq'
  constant.FedML_FEDERATED_OPTIMIZER_FEDOPT_SEQ = 'FedOpt_seq'
  constant.FedML_FEDERATED_OPTIMIZER_FEDGKT = 'FedGKT'
  constant.FedML_FEDERATED_OPTIMIZER_FEDNAS = 'FedNAS'
  constant.FedML_FEDERATED_OPTIMIZER_FEDSEG = 'FedSeg'
  constant.FedML_FEDERATED_OPTIMIZER_TURBO_AGGREGATE = 'turbo_aggregate'
  constant.FedML_FEDERATED_OPTIMIZER_FEDNOVA = 'FedNova'
  constant.FedML_FEDERATED_OPTIMIZER_HIERACHICAL_FL = 'HierarchicalFL'
  constant.FedML_FEDERATED_OPTIMIZER_FEDSGD = 'FedSGD'
  constant.FedML_FEDERATED_OPTIMIZER_FEDLOCALSGD = 'FedLocalSGD'
  constant.FedML_FEDERATED_OPTIMIZER_ASYNC_FEDAVG = 'Async_FedAvg'
})(constant || (constant = {}))
