# Definitions of sweep parameters.

from xenon.base.datatypes import IntParam, StrParam, BoolParam

PARTITION = "partition"
BLOCK = "block"
CYCLIC = "cyclic"
COMPLETE = "complete"
SPAD = "spad"
CACHE = "cache"
NO_UNROLL = 1
FLATTEN = 0

def shortSizeToInt(size_str):
  """ Go from 16kB -> 16384. """
  if size_str.endswith("kB"):
    return int(size_str[:-2])*1024
  elif size_str.endswith("MB"):
    return int(size_str[:-2])*1024*1024
  elif size_str.endswith("GB"):
    return int(size_str[:-2])*1024*1024*1024
  elif size_str.endswith("B"):
    # If we're dealing with anything larger than what can be expressed in GB,
    # there's a problem.
    return int(size_str[:-2])
  else:
    raise ValueError("Size \"%s\" cannot be converted into bytes." % size_str)

def intToShortSize(size):
  """ Go from 16384 -> 16kB. """
  if size < 1024:
    return str(size)
  else:
    return "%dkB" % (size/1024)

# Core Aladdin parameters.
cycle_time = IntParam("cycle_time", 1)
unrolling = IntParam("unrolling", 1)
partition_factor = IntParam("partition_factor", 1)
partition_type = StrParam("partition_type", CYCLIC,
                          valid_opts=[COMPLETE, CYCLIC, BLOCK])
# Aladdin currently only accepts integer values.
pipelining = IntParam("pipelining", 0)
memory_type = StrParam("memory_type", SPAD, valid_opts=[SPAD, CACHE])

# Cache memory system parameters.
cache_size = IntParam("cache_size", 32 * 1024, format_func=intToShortSize)
cache_assoc = IntParam("cache_assoc", 8)
cache_hit_latency = IntParam("cache_hit_latency", 4)
cache_line_sz = IntParam("cache_line_sz", 64)
cache_queue_size = IntParam("cache_queue_size", 32)
cache_bandwidth = IntParam("cache_bandwidth", 4)
tlb_hit_latency = IntParam("tlb_hit_latency", 20)
tlb_miss_latency = IntParam("tlb_miss_latency", 20)
tlb_page_size = IntParam("tlb_page_size", 4096)
tlb_entries = IntParam("tlb_entries", 8)
tlb_max_outstanding_walks = IntParam("tlb_max_outstanding_walks", 8)
tlb_assoc = IntParam("tlb_assoc", 0)
tlb_bandwidth = IntParam("tlb_bandwidth", 4)
perfect_l1 = IntParam("perfect_l1", 0)
perfect_bus = IntParam("perfect_bus", 0)
link_latency = IntParam("link_latency", 1)
link_width_bits = IntParam("link_width_bits", 512)

l0d_size = IntParam("l0d_size", 32*1024, format_func=intToShortSize)
l0d_assoc = IntParam("l0d_assoc", 8)
l0d_hit_latency = IntParam("l0d_hit_latency", 4)
l0i_size = IntParam("l0i_size", 32*1024, format_func=intToShortSize)
l0i_assoc = IntParam("l0i_assoc", 8)
l0i_hit_latency = IntParam("l0i_hit_latency", 2)
l1d_size = IntParam("l1d_size", 1024*1024, format_func=intToShortSize)
l1d_assoc = IntParam("l1d_assoc", 8)
l1d_hit_latency = IntParam("l1d_hit_latency", 12)
l2_size = IntParam("l2_size", 32*1024*1024, format_func=intToShortSize)
l2_assoc = IntParam("l2_assoc", 16)
l2_hit_latency = IntParam("l2_hit_latency", 46)

# DMA settings.
dma_setup_overhead = IntParam("dma_setup_overhead", 30)
max_dma_requests = IntParam("max_dma_requests", 40)
dma_chunk_size = IntParam("dma_chunk_size", 64)
pipelined_dma = IntParam("pipelined_dma", 0)
ready_mode = IntParam("ready_mode", 0)
dma_multi_channel = IntParam("dma_multi_channel", 0)
ignore_cache_flush = IntParam("ignore_cache_flush", 0)
invalidate_on_dma_store = BoolParam("invalidate_on_dma_store", True)

# CPU only
cpu_only = BoolParam("cpu_only", False)