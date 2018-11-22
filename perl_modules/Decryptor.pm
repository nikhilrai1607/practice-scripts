package DECRYTOR;

use strict;
use Exporter qw(import);

our $VERSION     = 1.00;
our @ISA         = qw(Exporter);
our @EXPORT_OK   = qw(func1 func2);
our %EXPORT_TAGS = ( DEFAULT => [qw(func1)],
                 Both    => [qw(func1 func2)]);

sub func1  { return reverse @_  }
sub func2  { return map{ uc }@_ }

1;
