use strict;
use warnings;


my @array = (3,1,4,1,5,9,2,6,5,3);

my @sorted = qsort(@array);

print "@sorted\n";

sub qsort {
    my @arr =  @_;
	return if ($#arr < 0);
    my $pivot = shift @arr;
	my (@less, @great);
	foreach my $i (@arr) {
	    if($i >= $pivot) {
		    push(@great,$i);
		}
		else {
		    push(@less,$i);
		}
	}
	return (qsort(@less),$pivot,qsort(@great));
}