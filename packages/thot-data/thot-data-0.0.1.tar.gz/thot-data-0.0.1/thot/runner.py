
# coding: utf-8

# # Runner

# In[1]:


import os
import sys
import subprocess

from .thot import LocalProject


# In[2]:


def run_program( program, container ):
    """
    Runs the given program form the given Container.
    
    :param program: Program to run.
    :param container: ID of the container to run from.
    """
    # setup environment
    env = os.environ.copy()
    
    # set root container to be used by thot library
    env[ 'THOT_CONTAINER_ID' ] = container
    
    # TODO [0]: Ensure safely run
    # run program
    subprocess.call(
        'python {}'.format( program ),
        shell = True,
        env = env
    )
    
    
def run_local( root ):
    """
    Runs programs bottom up for local projects.
    
    :param root: Path to root.
    """
    def eval_tree( root ):
        root = db.find_container( { '_id': root } )
        
        # eval children
        for child in root.children:
            eval_tree( child )

        # eval self
        scripts = root.scripts
        scripts.sort()
        for script in scripts:
            if not script.autorun:
                continue
            
            path = os.path.normpath( # path to scri
                os.path.join( script._id, script.script )
            )
            
            # used to set local properties
            os.environ[ 'THOT_SCRIPT_ID' ]     = script._id
            os.environ[ 'THOT_SCRIPT_SCRIPT' ] = path
            
            run_program( path, root._id )
    
    db = LocalProject( root )
    eval_tree( root )


# In[4]:


if __name__ == '__main__':
    """
    Runs a Thot Project from console.
    """
    from argparse import ArgumentParser
    
    parser = ArgumentParser( description = 'Thot project runner for Python.' )
    
    parser.add_argument(
        '-r', '--root',
        type = str,
        default = '.',
        help = 'Path of root Container.'
    )
    
    parser.add_argument(
        '-env', '--environment',
        type = str,
        choices = [ 'local', 'hosted' ],
        default = 'local',
        help = 'Environment of the runner.'
    )
    
    args = parser.parse_args()

    if args.environment == 'local':
        run_local( os.path.abspath( args.root ) )


# # Work

# In[4]:


# root = os.path.normpath(
#     os.path.join( os.getcwd(), '../_tests/projects/inclined-plane' )
# )

# run_local( root )

