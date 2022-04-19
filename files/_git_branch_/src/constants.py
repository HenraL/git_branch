#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## hello_world
## File description:
## constants.py
##

__Author__ = "Henry Letellier"
__Program_Name__ = "Git Branch"

import platform, sys

current_os = platform.system()

# Color class related vars
colorise_output = True
# The final reference created depending on if you are unser windows or not
colour_pallet = dict()
default_background = '0'
default_foreground = 'A'
windows_colour_command = "color "
non_windows_colour_command = "echo -e "
# Windows Color pallet (+ r (equivalent to a 'color AA'))
options_for_colour_pallet = "042615378CAE9DBFr"
options_for_testing_colour_pallet = "0123456789ABCDEFr"
non_windows_colours = []
# Create colour list
for i in range(30,38):
    non_windows_colours.append(f"{i}")
for i in range(90, 98):
    non_windows_colours.append(f"{i}")
non_windows_colours.append("0")


# Git_branch related vars

current_system = platform.system()
argv = sys.argv
argc = len(argv)
available_commands = ["h", "q"]
full_commands = dict()
# help command
for i in ["h", "help","?","/?"]:
    full_commands[i] = "help"
# quit command
for i in ["q", "quit", "exit"]:
    full_commands[i] = "quit"
# change branch command
for i in ["change_branch","chb","ch_b","chbr","ch_br"]:
    full_commands[i] = "change_branch"
# merge branch command (still needs to be finished)
for i in ["merge_branch","mrg","mer","mrg_br","mrg_b", "mb","m_b","mebr","me_br"]:
    full_commands[i] = "merge_branch"
# create branch command
for i in ["create_branch","crb","cr_b","crbr","cr_br"]:
    full_commands[i] = "create_branch"
# push branch command
for i in ["push_branch","p_b","push","pbr","p_br", "pu_br", "pubr", "pb"]:
    full_commands[i] = "push_branch"
# push to branch command
full_commands["push_to_branch"]="push_to_branch"
full_commands["ptb"]="push_to_branch"
full_commands["p_t_b"]="push_to_branch"
full_commands["putobr"]="push_to_branch"
full_commands["pu_to_br"]="push_to_branch"
# create and change command
full_commands["create_and_change"]="create_and_change"
full_commands["cac"]="create_and_change"
full_commands["c_a_c"]="create_and_change"
full_commands["cranch"]="create_and_change"
full_commands["cr_an_ch"]="create_and_change"
# list all branches command
full_commands["list_all_branches"]="list_all_branches"
full_commands["lab"]="list_all_branches"
full_commands["l_a_b"]="list_all_branches"
full_commands["lialbr"]="list_all_branches"
full_commands["li_al_br"]="list_all_branches"
# list local branches command
full_commands["list_local_branches"]="list_local_branches"
full_commands["llb"]="list_local_branches"
full_commands["l_l_b"]="list_local_branches"
full_commands["lilobr"]="list_local_branches"
full_commands["li_lo_br"]="list_local_branches"
# rename local branch command
full_commands["rename_local_branch"]="rename_local_branch"
full_commands["rlb"]="rename_local_branch"
full_commands["r_l_b"]="rename_local_branch"
full_commands["relobr"]="rename_local_branch"
full_commands["re_lo_br"]="rename_local_branch"
# delete local branch command
full_commands["delete_local_branch"]="delete_local_branch"
full_commands["dlb"]="delete_local_branch"
full_commands["d_l_b"]="delete_local_branch"
full_commands["delobr"]="delete_local_branch"
full_commands["de_lo_br"]="delete_local_branch"
# delete remote branch command
full_commands["delete_remote_branch"]="delete_remote_branch"
full_commands["drb"]="delete_remote_branch"
full_commands["d_r_b"]="delete_remote_branch"
full_commands["derebr"]="delete_remote_branch"
full_commands["de_re_br"]="delete_remote_branch"
# rename remote branch command
full_commands["rename_remote_branch"]="rename_remote_branch"
full_commands["rrb"]="rename_remote_branch"
full_commands["r_r_b"]="rename_remote_branch"
full_commands["rerebr"]="rename_remote_branch"
full_commands["re_re_br"]="rename_remote_branch"
# list remote branches command
full_commands["list_remote_branches"]="list_remote_branches"
full_commands["lrb"]="list_remote_branches"
full_commands["l_r_b"]="list_remote_branches"
full_commands["lirebr"]="list_remote_branches"
full_commands["li_re_br"]="list_remote_branches"
# force remote local branch command
full_commands["force_rename_local_branch"]="force_rename_local_branch"
full_commands["frlb"]="force_rename_local_branch"
full_commands["f_r_l_b"]="force_rename_local_branch"
full_commands["forelobr"]="force_rename_local_branch"
full_commands["fo_re_lo_br"]="force_rename_local_branch"
# force delete local branch command
full_commands["force_delete_local_branch"]="force_delete_local_branch"
full_commands["fdlb"]="force_delete_local_branch"
full_commands["f_d_l_b"]="force_delete_local_branch"
full_commands["fodelobr"]="force_delete_local_branch"
full_commands["fo_de_lo_br"]="force_delete_local_branch"
# force delete remote branch command
full_commands["force_delete_remote_branch"]="force_delete_remote_branch"
full_commands["fdrb"]="force_delete_remote_branch"
full_commands["f_d_r_b"]="force_delete_remote_branch"
full_commands["foderebr"]="force_delete_remote_branch"
full_commands["fo_de_re_br"]="force_delete_remote_branch"
# force rename remote branch command
full_commands["force_rename_remote_branch"]="force_rename_remote_branch"
full_commands["frrb"]="force_rename_remote_branch"
full_commands["f_r_r_b"]="force_rename_remote_branch"
full_commands["forerebr"]="force_rename_remote_branch"
full_commands["fo_re_re_br"]="force_rename_remote_branch"
# search local branch command
full_commands["search_local_branch_by_commit"]="search_local_branch_by_commit"
full_commands["slbbc"]="search_local_branch_by_commit"
full_commands["s_l_b_b_c"]="search_local_branch_by_commit"
full_commands["selobrbyco"]="search_local_branch_by_commit"
full_commands["se_lo_br_by_co"]="search_local_branch_by_commit"
# rename remote and local branch command
full_commands["rename_remote_and_local_branch"]="rename_remote_and_local_branch"
full_commands["rralb"]="rename_remote_and_local_branch"
full_commands["r_r_a_l_b"]="rename_remote_and_local_branch"
full_commands["rereanlobr"]="rename_remote_and_local_branch"
full_commands["re_re_an_lo_br"]="rename_remote_and_local_branch"
# search remote branch by commit command
full_commands["search_remote_branch_by_commit"]="search_remote_branch_by_commit"
full_commands["srbbc"]="search_remote_branch_by_commit"
full_commands["s_r_b_b_c"]="search_remote_branch_by_commit"
full_commands["serebrbyco"]="search_remote_branch_by_commit"
full_commands["se_re_br_by_co"]="search_remote_branch_by_commit"
# force rename remote and local branch command
full_commands["force_rename_remote_and_local_branch"]="force_rename_remote_and_local_branch"
full_commands["frralb"]="force_rename_remote_and_local_branch"
full_commands["f_r_r_a_l_b"]="force_rename_remote_and_local_branch"
full_commands["forereanlobr"]="force_rename_remote_and_local_branch"
full_commands["fo_re_re_an_lo_br"]="force_rename_remote_and_local_branch"
# search remote and local branch by commit command
full_commands["search_remote_and_local_branch_by_commit"]="search_remote_and_local_branch_by_commit"
full_commands["sralbbc"]="search_remote_and_local_branch_by_commit"
full_commands["s_r_a_l_b_b_c"]="search_remote_and_local_branch_by_commit"
full_commands["sereanlobrbyco"]="search_remote_and_local_branch_by_commit"
full_commands["se_re_an_lo_br_by_co"]="search_remote_and_local_branch_by_commit"

# "merge_branch"
# "create_branch"
# "push_to_branch"
# "create_and_change"
# "list_all_branches"
# "list_local_branches"
# "rename_local_branch"
# "delete_local_branch"
# "delete_remote_branch"
# "rename_remote_branch"
# "list_remote_branches"
# "force_rename_local_branch"
# "force_delete_local_branch"
# "force_delete_remote_branch"
# "force_rename_remote_branch"
# "search_local_branch_by_commit"
# "rename_remote_and_local_branch"
# "search_remote_branch_by_commit"
# "force_rename_remote_and_local_branch"
# "search_remote_and_local_branch_by_commit"
