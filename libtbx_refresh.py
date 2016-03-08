import os
from annlib_adaptbx.source_generators import generate_all

if (self.env.is_ready_for_build()):
  message = '  Generating C++ files for self-inclusive approximate nearest neighbor'
  print message
  for search_mode in ["self_include"]:
    for item in generate_all.yield_includes(search_mode):
      #print item
      G = open(item['src'],'r')
      lines = G.readlines()
      G.close()
      generate_all.process_includes(lines,search_mode)
      F = open(item['dst'],'w')
      F.write(''.join(lines))
      F.close()

    for item in generate_all.yield_src_includes(search_mode):
      #print item
      G = open(item['src'],'r')
      lines = G.readlines()
      G.close()
      generate_all.process_src_includes(lines,search_mode)
      F = open(item['dst'],'w')
      F.write(''.join(lines))
      F.close()

    for item in generate_all.yield_src(search_mode):
      #print item
      G = open(item['src'],'r')
      lines = G.readlines()
      G.close()
      generate_all.process_src(lines,search_mode,os.path.basename(item['src']))
      F = open(item['dst'],'w')
      F.write(''.join(lines))
      F.close()
