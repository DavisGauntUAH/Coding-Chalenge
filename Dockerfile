FROM jupyter/base-notebook





#RUN apt-get install python

# RUN python ./longest_substring/longest_substring.py
# RUN python ./next_permutation/next_perm.py
# RUN python ./reverse_nodes/reverse_nodes.py
# RUN python ./two_numbers/two_numbers.py
# RUN python ./zig_zag/zig_zag.py



USER jovyan
WORKDIR /home/jovyan

COPY . /home/jovyan/app
COPY ./examples /home/jovyan/
USER root
RUN chmod 777 ./app
USER jovyan

RUN cd app && python setup.py install

# ENV JUPYTER_ENABLE_LAB=no
# CMD ["echo", "worked"]
