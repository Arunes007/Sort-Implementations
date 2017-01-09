##!/usr/bin/perl
use strict;
use warnings;

my @array = (12,11,13,5);

print "Before Sort: [@array]\n";

merge_sort( \@array, 0, $#array );

print "After  Sort: [@array]\n";

sub merge_sort {
    my ( $ar, $p, $r ) = @_;
    if( $p  < $r ) {
        my $q = int( ($p + $r) / 2);
        # divide
        merge_sort( $ar, $p, $q );
        # divide
        merge_sort( $ar, $q + 1 , $r );
        # conquer
        merge( $ar, $p, $q, $r );
    }
}


sub merge {
    my ( $ar, $p, $q, $r ) = @_;

    # divide into two left and right subarrays
    my @left = @$ar[$p .. $q];
    my @right = @$ar[$q + 1 .. $r];

    # intialize
    my $i = my $j = 0;

    # now compare both left and half arrays
    for my $k ($p .. $r) {
        # This check just for sentinals
        if(@right and @left) {
            #print "@right\n";
            if( $left[$i] <= $right[$j] ) {
                $ar -> [$k] = shift @left;
            }
            else {
                $ar -> [$k] = shift @right;
            }
        }
        elsif(@left and !@right) {
            $ar -> [$k] = shift @left;
        }
        elsif(!@left and @right) {
            $ar -> [$k] = shift @right;
        }
    }
}
