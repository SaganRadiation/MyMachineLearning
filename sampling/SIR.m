%This is an implementation of sampling importance resampling.
%The Hidden Markov Model has only two states for both latent
%and evidence variables.
%len = number of evidence to generate
%parts = number of particles to use
%trans = transmission probability (float)
%emit = emission probability (float)
%example usage: SIR(300, 100, .7, .8)

function SIR(len,parts,trans,emit)
    tr = [trans 1-trans; 1-trans trans];
    e = [emit 1 - emit; 1 - emit emit];
    
    [x y] = hmmgenerate(len,tr,e);
    
    out = zeros(parts,len);
    w = zeros(parts,1);
    for n=1:parts,
        out(n,1) = binornd(1,0.5) + 1;
    end
    for t=2:len
        for n=1:parts;
              out(n,t) = binornd(1, 1 - tr( out(n,(t-1)) ,1) ) + 1;
              w(n) = e( out(n,t), y(t));
        end
        
        w = w/sum(w);
        out(:,t) = randsample(out(:,t),parts,true,w);
        t = t+1;
    end
    guess = mode(out);
    figure(1); clf;
    hold on;
    scatter(1:length(y),guess,'b');
    scatter(1:length(y),x,15,'r');
    axis([0 30 .5 2.5]);
    fprintf('Accuracy is %i%%\n',round(sum(x==guess)/len * 100))
