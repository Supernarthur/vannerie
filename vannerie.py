#!/usr/bin/env python3

import sys
import csv


def put_brin(nb_enf, brin_len, brin_pos, forward):
    """
    :param nb_enf: int, nombre d'enfonçures (sans rives)
    :param brin_len: int, longueur du brin en espaces entre 2 enfonçures
    :param brin_pos: int, enfonçure à laquelle le brin commence
    :param forward: bool, sens du brin (True pour >, False pour <)
    :return: tuple, (brin_pos finale, forward/backwards)
    """
    # print("put_brin: len = %s, pos = %s, forward = %s" %
    #      (brin_len, brin_pos, forward))
    if forward:
        to_rive = nb_enf + 1 - brin_pos
        if brin_len < to_rive:
            return (brin_pos + brin_len, True)
        elif brin_len == to_rive:
            """
            Cas spécial : quand l'algo s'arrête sur la rive, on
            choisit de s'arrêter sur l'enfonçure suivante
            """
            return (nb_enf, False)
        else:
            return put_brin(nb_enf, brin_len - to_rive,
                            nb_enf + 1, False)
    if not forward:
        to_rive = brin_pos
        if brin_len < to_rive:
            return (brin_pos - brin_len, False)
        elif brin_len == to_rive:  # same shit, see above
            return (1, True)
        else:
            return put_brin(nb_enf, brin_len - to_rive,
                            0, True)


def make_pattern(nb_enf, brin_len, start_pos, forward=True):
    """
    :param nb_enf: int, nombre d'enfonçures (sans rives)
    :param brin_len: int, longueur du brin en espaces entre 2 enfonçures
    :param start_pos: int, enfonçure à laquelle le pattern commence
    :param forward: bool, sens du brin au départ (True pour >, False pour <)
    :return: list d'ints, start_pos de chaque brin, négatif si sens <
    """
    pattern = []
    brin_pos = start_pos
    for i in range(50):
        # print("brin %s: start_pos = %s, forward = %s" %
        #     (i, brin_pos, forward))
        if forward:
            pattern.append(brin_pos)
        else:
            pattern.append(-brin_pos)
        brin_pos, forward = put_brin(nb_enf, brin_len, brin_pos, forward)
        if brin_pos == pattern[0]:
            break
    return pattern


def main():
    output = []
    for nb_enf in range(8, 20 + 1):
        for brin_len in range(8, 24 + 2, 2):
            for start_pos in range(1, nb_enf + 1):
                pattern = make_pattern(nb_enf, brin_len, start_pos)
                output.append([
                        nb_enf,
                        brin_len,
                        start_pos,
                        len(pattern)
                    ] + pattern)

    with open(sys.argv[1], 'w') as fd:
        header = ["Nombre d'enfoncures",
                  "Longueur du brin",
                  "Enfoncure de depart",
                  "Nombre de brins par cycle"]
        header += ["Brin" + str(i) for i in range(51)]
        writer = csv.writer(fd)
        writer.writerow(header)
        for row in output:
            writer.writerow(row)


if __name__ == '__main__':
    main()
