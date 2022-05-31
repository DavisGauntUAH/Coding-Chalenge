FROM python:3.9
COPY . /app
WORKDIR /app
RUN python setup.py install
# RUN python ./longest_substring/longest_substring.py
# RUN python ./next_permutation/next_perm.py
# RUN python ./reverse_nodes/reverse_nodes.py
# RUN python ./two_numbers/two_numbers.py
# RUN python ./zig_zag/zig_zag.py